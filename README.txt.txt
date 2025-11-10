===========================================
LAB RPC - Programação Paralela e Distribuída
===========================================

Alunos:
- Marcel Santana - 2213291
- Arthur Manenti - 2212320

Linguagem: Python
Tema: Calculadora Distribuída via gRPC
Bibliotecas: grpcio, grpcio-tools, pybreaker

-------------------------------------------
1️⃣ Instalar dependências:
pip install -r requirements.txt

2️⃣ Gerar arquivos gRPC:
python -m grpc_tools.protoc -Iproto --python_out=server --grpc_python_out=server proto/calculator.proto
python -m grpc_tools.protoc -Iproto --python_out=client --grpc_python_out=client proto/calculator.proto

3️⃣ Iniciar servidor:
cd server
python server.py

4️⃣ Em outro terminal, iniciar cliente:
cd client
python client.py

-------------------------------------------
🎥 Testes obrigatórios para vídeo de entrega:
✅ Soma, subtração, multiplicação e divisão (incluindo divisão por zero)
⚠️ Desligar o servidor → cliente exibe erro e ativa Circuit Breaker
♻️ Ligar o servidor novamente → cliente volta a funcionar após reset_timeout (5s)
