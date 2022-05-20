from rest_framework import status
from rest_framework import views
from rest_framework.response import Response
from transactions import constants
from transactions import services


class MCMAPIView(views.APIView):
    service_class = services.LowestCommonMultipleService

    def get(self, request, *args, **kwargs):
        query_numbers = request.query_params.get('numbers', [])
        split_list = query_numbers.split(',')
        mcm_service = self.service_class(split_list)
        parse_numbers = mcm_service.parse_list()
        if not parse_numbers:
            return Response({"message": constants.INCORRECT_NUMBERS_FORMAT}, status=status.HTTP_400_BAD_REQUEST)
        mcm_service.list_numbers = parse_numbers
        result = mcm_service.lowest_common_multiple()
        if not result:
            return Response({"message": constants.INTERNAL_SERVER_ERROR}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response({"mcm": result}, status=status.HTTP_200_OK)


class PlusOneView(views.APIView):
    service_class = services.ReturnPlusOneService

    def get(self, request, *args, **kwargs):
        number = request.query_params.get('number', 0)
        plus_service = self.service_class(number)
        parse_number = plus_service.parse_number()
        if not parse_number:
            return Response({"message": constants.INCORRECT_NUMBER_FORMAT}, status=status.HTTP_400_BAD_REQUEST)
        plus_service.number = parse_number
        result = plus_service.add_one()
        if not result:
            return Response({"message": constants.INTERNAL_SERVER_ERROR}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response({"added_number": result}, status=status.HTTP_200_OK)
