class TransactionHistoryService():

    def get_all_by_user_id(self, user_id, data, model):
        try:
            filter = {"UserId": user_id}
            if data is not None:
                filter["Description"] = data

            return model.get_all_by(filter)

        except Exception as e:
            return None,  -1, f'Exception as {str(e)}'