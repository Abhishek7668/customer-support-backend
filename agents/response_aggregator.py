class ResponseAggregator:

    @staticmethod
    def aggregate(agent_responses):

        """
        Converts multiple agent responses
        into one formatted context.
        """

        context = ""

        for response in agent_responses:

            context += f"""

Agent : {response['agent']}

Response :

{response['response']}

"""

        return context.strip()