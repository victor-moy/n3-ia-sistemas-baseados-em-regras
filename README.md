# Sistemas Baseados em Regras

Trabalho da disciplina de **Inteligência Artificial** — N3  
**Professor:** Claudinei Dias (Ney) · **Semestre:** 2026/1

---

## Sobre

Sistema Especialista de Triagem Médica desenvolvido em Python, demonstrando os conceitos de **Sistemas Baseados em Regras** com motor de inferência por **encadeamento para frente** (Forward Chaining).

O sistema analisa sintomas informados pelo usuário, aplica 10 regras de produção e apresenta o diagnóstico mais provável junto com a cadeia de inferência utilizada.

## Como executar

**Interface web (recomendado)**

```bash
pip install flask
python demo/app.py
```

Acesse `http://localhost:5000` no navegador.

**Interface de linha de comando**

```bash
python demo/sistema_especialista.py
```

> Requer Python 3.7+. Sem dependências além do Flask para a interface web.

## Estrutura

```
demo/
├── sistema_especialista.py   # motor de regras + CLI
├── app.py                    # servidor Flask
├── requirements.txt
└── templates/index.html      # interface web

relatorio/
└── relatorio.pdf             # relatório completo

slides/
└── slides.md                 # roteiro da apresentação
```

## Integrantes

- Laíza Silva  
- Jhessica Alves  
- Victor Moy
