# ==============================================
# Trabalho PPD - RPC
# Alunos:
#   Marcel Santana - 2213291
#   Arthur Manenti - 2212320
# ==============================================

import grpc
from concurrent import futures
import calculator_pb2
import calculator_pb2_grpc

class CalculatorService(calculator_pb2_grpc.CalculatorServicer):
    def Add(self, request, context):
        result = request.numOne + request.numTwo
        print(f"Soma: {request.numOne} + {request.numTwo} = {result}")
        return calculator_pb2.Result(value=result, message="Operação realizada com sucesso")

    def Subtract(self, request, context):
        result = request.numOne - request.numTwo
        print(f"Subtração: {request.numOne} - {request.numTwo} = {result}")
        return calculator_pb2.Result(value=result, message="Operação realizada com sucesso")

    def Multiply(self, request, context):
        result = request.numOne * request.numTwo
        print(f"Multiplicação: {request.numOne} * {request.numTwo} = {result}")
        return calculator_pb2.Result(value=result, message="Operação realizada com sucesso")

    def Divide(self, request, context):
        if request.numTwo == 0:
            return calculator_pb2.Result(value=0, message="Erro: divisão por zero")
        result = request.numOne / request.numTwo
        print(f"Divisão: {request.numOne} / {request.numTwo} = {result}")
        return calculator_pb2.Result(value=result, message="Operação realizada com sucesso")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    calculator_pb2_grpc.add_CalculatorServicer_to_server(CalculatorService(), server)
    server.add_insecure_port('[::]:8080')
    server.start()
    print("Servidor gRPC ativo na porta 8080")
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
