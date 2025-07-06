from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Expense
from django.views.decorators.http import require_GET,require_http_methods

@csrf_exempt
def submit_expense(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)

            description = data.get("description")
            amount = data.get("amount")
            category = data.get("category", "")  # optional for now

            expense = Expense.objects.create(
                description=description,
                amount=amount,
                category=category
            )       
# 
            return JsonResponse({
                "message": "Expense saved successfully",
                "expense": {
                    "id": expense.id,
                    "description": expense.description,
                    "amount": expense.amount,
                    "category": expense.category,
                    "date": expense.date,
                }
            })

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"error": "Only POST method allowed"}, status=405)


@require_GET
def hello_world(request):
    return JsonResponse({"message": "Hello World from Expense Tracker API"})

@require_GET
def get_all_expenses(request):
    expenses = Expense.objects.all().order_by('-date')  # latest first
    datf = [
        {
            "id": expense.id,
            "description": expense.description,
            "amount": expense.amount,
            "category": expense.category,
            "date": expense.date,
        }
        for expense in expenses
    ]
    return JsonResponse({"expenses": datf}, safe=False)

@csrf_exempt
@require_http_methods(["DELETE"])
def delete_expense(request, expense_id):
    try:
        expense = Expense.objects.get(pk=expense_id)
        expense.delete()
        return JsonResponse({"message": f"Expense with id {expense_id} deleted successfully"})
    except Expense.DoesNotExist:
        return JsonResponse({"error": "Expense not found"}, status=404)