---
id: "39359330507287"
titulo: "Erro COM_E00560: Não é possível usar variáveis nos filtros na Ficha de Parceiros (Giro Negociações)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39359330507287-Erro-COM-E00560-N%C3%A3o-%C3%A9-poss%C3%ADvel-usar-vari%C3%A1veis-nos-filtros-na-Ficha-de-Parceiros-Giro-Negocia%C3%A7%C3%B5es"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-08-31T02:48:46Z"
rotulos: ["Configuração", "Parceiro", "Movimentação Financeira", "Financeiro", "Erro", "Artigo criado KCS", "CVE - KCS"]
---

# Erro COM_E00560: Não é possível usar variáveis nos filtros na Ficha de Parceiros (Giro Negociações)

**Mensagem**

**[COM\_E00560] Não é possível usar variáveis nos filtros**

**Situação**

Este erro pode ocorrer quando o usuário tenta criar um filtro dentro da ficha de parceiros (Giro de Negociações), onde está configurado para usar variáveis.

**Solução**

Para resolver este erro, siga os passos abaixo:

**(1)** Acesse **Ficha de Parceiros**.

**(2)** No painel **Giro de Negociações**, role até o final e abra o **Filtro Personalizado**.

**(3)** Abra o **Assistente de Filtros** e localize o filtro marcado como ativo.

**(4)** Se a expressão contiver um `?`, remova esse parâmetro:

- Substitua por um valor fixo, ou
- (se aplicável) use a opção específica de "usuário logado" do assistente, em vez de digitar o parâmetro manualmente.

**(5)** Salve o filtro novamente e teste o Giro de Negociações.

**Causa**

O Filtro Personalizado do painel Giro de Negociações (Ficha de Parceiros) não aceita parâmetros dinâmicos representados pelo caractere `?` na expressão SQL. Se o filtro ativo tiver sido salvo com esse tipo de parâmetro, o sistema bloqueia a consulta e exibe esse erro.

(pendente sua confirmação: "A única variável aceita é o usuário logado, disponível como opção própria no Assistente de Filtros, ela não é digitada manualmente como '?'.")
