# ==============================================
# Trabalho PPD - RPC
# Alunos:
#   Marcel Santana - 2213291
#   Arthur Manenti - 2212320
# ==============================================

import grpc
import calculator_pb2
import calculator_pb2_grpc
import pybreaker

breaker = pybreaker.CircuitBreaker(fail_max=2, reset_timeout=5)

@breaker
def do_operation(client, op, x, y):
    if op == 1:
        return client.Add(calculator_pb2.Numbers(numOne=x, numTwo=y))
    elif op == 2:
        return client.Subtract(calculator_pb2.Numbers(numOne=x, numTwo=y))
    elif op == 3:
        return client.Multiply(calculator_pb2.Numbers(numOne=x, numTwo=y))
    elif op == 4:
        return client.Divide(calculator_pb2.Numbers(numOne=x, numTwo=y))

def main():
    channel = grpc.insecure_channel('localhost:8080')
    client = calculator_pb2_grpc.CalculatorStub(channel)
    print("Cliente gRPC conectado ao servidor Calculator.\n")

    while True:
        print("\nSelecione a operação:")
        print("1) Soma")
        print("2) Subtração")
        print("3) Multiplicação")
        print("4) Divisão")
        print("0) Sair")

        try:
            op = int(input("> "))
            if op == 0:
                break
            if op not in [1,2,3,4]:
                print("Opção inválida.")
                continue

            x = float(input("Digite o primeiro número: "))
            y = float(input("Digite o segundo número: "))

            response = do_operation(client, op, x, y)
            print(f"Resultado: {response.value} | {response.message}")

        except pybreaker.CircuitBreakerError:
            print("⚠️ Circuit Breaker ativo — servidor indisponível, tentando novamente...")
        except grpc.RpcError:
            print("Erro de comunicação RPC com o servidor.")
        except ValueError:
            print("Entrada inválida, use números.")
        except Exception as e:
            print("Erro:", e)

if __name__ == "__main__":
    main()
