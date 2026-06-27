# Sistema Especialista de Triagem Médica Básica

Sistema Baseado em Regras com encadeamento para frente (Forward Chaining), desenvolvido em Python.

## Interface Web (recomendado para demo)

```bash
pip install -r requirements.txt
python app.py
```

Acesse **http://127.0.0.1:5000** no navegador.

## Interface de Linha de Comando

```bash
python sistema_especialista.py
```

> Requer Python 3.7+. Sem dependências externas.

## Como funciona

O sistema coleta sintomas do usuário via terminal, aplica as regras da base de conhecimento usando encadeamento para frente e apresenta o diagnóstico mais provável com a cadeia de inferência utilizada.

## Estrutura

| Componente | Descrição |
|---|---|
| `REGRAS` | Base de conhecimento com 10 regras de produção |
| `TODOS_SINTOMAS` | Lista de fatos possíveis (sintomas) |
| `coletar_fatos()` | Interface com o usuário (coleta de dados) |
| `encadeamento_para_frente()` | Motor de inferência |
| `exibir_resultado()` | Exibe raciocínio e conclusão |
