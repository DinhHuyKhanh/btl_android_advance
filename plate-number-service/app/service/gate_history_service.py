class GateHistoryService():

    def get_all_gate_histories(self, user_id, model):
        return model.get_all_gate_histories(user_id)
    
    def create(self, data, model):
        return model.create(data)