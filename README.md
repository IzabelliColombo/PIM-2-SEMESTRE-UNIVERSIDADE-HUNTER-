# 🎓 Sistema Acadêmico Colaborativo (SAC)

> Projeto desenvolvido por alunos da **Universidade Paulista (UNIP)** como parte do **PIM – Projeto Integrado Multidisciplinar** do curso de **Análise e Desenvolvimento de Sistemas**.
>
> O **SAC (Sistema Acadêmico Colaborativo)** é um sistema criado para **melhorar a comunicação entre alunos e professores**, integrando ferramentas de **cadastro, fórum de dúvidas, acompanhamento de desempenho e interação digital**.
>
> Todo o sistema foi desenvolvido e codificado pelo grupo, aplicando conceitos práticos de **Engenharia de Software, Programação, Redes e Inteligência Artificial**.

---

## 🧠 Objetivo do Projeto
Criar um ambiente acadêmico colaborativo, sustentável e acessível, que facilite:
- 📚 A comunicação entre alunos e professores  
- 💬 O envio e resposta de dúvidas acadêmicas  
- 🧮 O controle de turmas, notas e matérias  
- 🌱 A eliminação do uso de papel, incentivando a educação digital

---

## ⚙️ Tecnologias Utilizadas
- **Linguagem:** Python 3  
- **Bibliotecas nativas:**  
  - `json` – para armazenamento e leitura de dados  
  - `os` – para manipulação de arquivos  
- **Persistência de dados:** arquivo `duvidas_forum.json`  
- **Interface:** menus interativos no terminal (CLI) com cores ANSI  

---

## 🗂️ Estrutura do Projeto

```
📦 SAC
├── sistema_academico.py        # Código principal do sistema
├── duvidas_forum.json          # Banco de dados local (dúvidas salvas)
└── README.md                   # Documentação do projeto
```

---

## 👩‍💻 Funcionalidades

### 👨‍🎓 Aluno
- Cadastro completo (nome, idade, RA, curso, contato)
- Escolha entre cursos disponíveis:
  - ADS (Análise e Desenvolvimento de Sistemas)
  - Engenharia de Software
  - Ciência da Computação
- Visualização de turmas e horários
- Fórum de Dúvidas:
  - Fazer perguntas por matéria
  - Acompanhar status (pendente/respondida)
  - Ver todas as dúvidas do fórum

---

### 👩‍🏫 Professor
- Cadastro com nome, disciplina e contato
- Visualização das turmas e horários atribuídos
- Acesso ao Fórum de Dúvidas:
  - Visualizar dúvidas pendentes
  - Responder perguntas dos alunos
  - Excluir dúvidas respondidas
  - Consultar o histórico de dúvidas

---

## 💾 Estrutura dos Dados (JSON)

As dúvidas são armazenadas no arquivo `duvidas_forum.json`:

```json
[
  {
    "aluno": "Izabelli Colombo",
    "ra": "R4280J9",
    "materia": "Python para Iniciantes",
    "pergunta": "Como funciona a função lambda?",
    "respondida": true,
    "resposta": "A função lambda é usada para criar funções anônimas em Python.",
    "professor": "Guilherme Mota"
  }
]
```

---

## 🔄 Fluxo de Funcionamento

1. O sistema pergunta se o usuário é **Aluno** ou **Professor**.  
2. Carrega as dúvidas existentes do arquivo JSON.  
3. Exibe menus específicos de acordo com o tipo de usuário.  
4. Todas as interações (novas dúvidas, respostas e exclusões) são salvas automaticamente.  
5. O programa permite retornar ao menu principal ou encerrar a qualquer momento.  

---

## 🧱 Estrutura e Conceitos Aplicados

- **Engenharia de Software (Scrum):** organização do projeto em sprints  
- **Programação Estruturada (C):** chatbot auxiliar (módulo complementar)  
- **Programação em Python:** módulo colaborativo e fórum  
- **Estrutura de Dados:** listas e dicionários para manipulação dos dados  
- **Redes de Computadores:** simulação de ambiente cliente-servidor (LAN)  
- **Educação Ambiental:** redução do uso de papel por meio da digitalização  

---

## 🌱 Sustentabilidade e Inovação

O SAC foi desenvolvido com foco na **sustentabilidade digital**, reduzindo o uso de papel e promovendo a comunicação online.  
Além disso, o sistema aplica conceitos de **Inteligência Artificial**, como o **chatbot em C**, que responde perguntas básicas dos alunos e auxilia no suporte automatizado.

---

## 🧩 Exemplo de Uso

```bash
$ python sistema_academico.py

===== SISTEMA ACADÊMICO INTEGRADO =====
Você é Aluno ou Professor? aluno

--- Cadastro de Aluno ---
Digite seu nome: Izabelli
Digite sua idade: 17
Digite seu RA: R4280J9
Digite seu e-mail: iza@example.com
Digite seu telefone: (11) 99999-9999
```

---

## 🧾 Autores do Projeto

👩‍💻 **Gabriely Da Silva Custódio** – RA: H788811  
👩‍💻 **Gabrielly Silva De Oliveira** – RA: H7514C3  
👨‍💻 **Guilherme de Jesus Mota** – RA: R960021  
👩‍💻 **Izabelli Turrubia Colombo** – RA: R4280J9  
👩‍💻 **Larissa Barbosa Marques** – RA: R8398C0  

---

## 🏫 Universidade Paulista – UNIP  
**Projeto Integrado Multidisciplinar (PIM)**  
Curso: *Análise e Desenvolvimento de Sistemas*  
Ano: **2025**  
Orientadores: Prof. Ageu e Prof. Eliana  

---

## 🪪 Licença
Este projeto foi desenvolvido para fins **educacionais e acadêmicos**, podendo ser reutilizado em contextos de aprendizado e pesquisa.  
© 2025 – Todos os direitos reservados ao grupo de autores.
