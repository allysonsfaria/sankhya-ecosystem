---
id: "32376126098967"
titulo: "Baixa de Títulos a Receber"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/32376126098967-Baixa-de-T%C3%ADtulos-a-Receber"
trilha: "Assistente de Melhores Práticas > Recebimentos"
atualizado_em: "2026-07-22T14:31:38Z"
rotulos: ["Configuração", "Contas", "Movimentação Financeira", "TOP", "Financeiro"]
---

# Baixa de Títulos a Receber

### Descrição

A funcionalidade **Baixa de Títulos a Receber** permite configurar os acessos dos responsáveis pelo processo de baixa de contas a receber, automatizando e controlando os registros de receitas recebidas no sistema.

Oferece os seguintes recursos:

- **Baixa Automática de Receitas:** Permite consultar, incluir, alterar e realizar a baixa automática de receitas.
- **Movimentação Financeira:** Disponibiliza funcionalidades para gerenciar receitas, incluindo consultas, alterações e estornos.
- **Estorno de Receitas:** Autoriza realizar o estorno de receitas já registradas no sistema.

### Como instalar

1. Clique em **"Iniciar"**.
2. Selecione os **"grupos e/ou usuários"** responsáveis pela baixa de contas a receber.
3. Clique em **"Avançar"** para revisar as informações.
4. Clique em **"Instalar"** para concluir a configuração.

### Detalhes da Instalação

**Acessos liberados**

- **"Baixa Automática de Receitas:"** Consultar, Incluir, Alterar, Excluir, Configurar, Filtro Avançado, Baixa de Receitas
- **"Movimentação Financeira:"** Consultar, Incluir, Alterar, Excluir, Configurar, Filtro Avançado, Baixa de Receitas, Estorno de Receitas

**Tabelas Atualizadas**

- **"TGFTOP – Tipos de Operação:"**
  - Inclusão da TOP **"1750 – Recebimento"**, se não existir.
  - Ativação da TOP criada.
- **"TSIUSU – Cadastro de Usuários:"**
  - Remoção do bloqueio "Inibe acesso a receitas" (campo CONTACESSO).
  - Atualização do campo TOPBAIXARECEITA para a TOP 1750 nos usuários selecionados.
