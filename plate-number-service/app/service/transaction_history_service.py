class TransactionHistoryService():

    def get_all_by_user_id(self, user_id, description, model):
        try:
            filter = {"UserId": user_id}
            if description is not None:
                filter["Description"] = description

            return model.get_all_by(filter)

        except Exception as e:
            return None,  -1, f'Exception as {str(e)}'
        
    def get_all_by_month_and_year(self, user_id, description, month, year, model):
        try:
            filter = {"UserId": user_id}
            if description is not None:
                filter["Description"] = description

            return model.get_transactions_by_month_and_year(month, year, filter)

        except Exception as e:
            return None,  -1, f'Exception as {str(e)}'