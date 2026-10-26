---
id: "24426984422423"
titulo: "Como configurar a exibição de Nome Fantasia ou Razão Social do Parceiro"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/24426984422423-Como-configurar-a-exibi%C3%A7%C3%A3o-de-Nome-Fantasia-ou-Raz%C3%A3o-Social-do-Parceiro"
trilha: "Solução de Problemas > Compras e Estoque"
atualizado_em: "2026-07-31T04:08:06Z"
rotulos: ["Configuração", "Parceiro", "Dicionário de Dados", "Preferências", "CORE_E06589", "Erro: campo 'NOME' não encontrado", "Configurações → Avançado → Preferências ajustar APRES.TGFVOL reiniciar sistema", "configuração incorreta do parâmetro", "Erro", "Artigo atualizado KCS", "CVE - KCS"]
---

# Como configurar a exibição de Nome Fantasia ou Razão Social do Parceiro

**SITUAÇÃO**

A preferência "NOMERAZAOPARC" foi configurada para exibir a Razão Social, porém o sistema continua apresentando o Nome Fantasia do parceiro. Mesmo após alterar essa preferência para a opção "Razão Social", telas como o Portal de Vendas/Compras (Gerente On-line) continuam exibindo o Nome Fantasia.

**SOLUÇÃO**

Para resolver este erro, corrija ou remova o parâmetro de apresentação da entidade parceiro. Siga os passos abaixo:

**(1)**  Acesse Configurações » Avançado » Preferências e confirme que o parâmetro **NOMERAZAOPARC – Apresentar Nome ou Razão Social do Parceiro** está definido como "Razão Social". Isso cobre o Portal de Vendas/Compras e as demais telas citadas na Causa.

**(2)** Se a Razão Social também precisar ser exibida nas Centrais (ex.: Central de Liberações, Central de Atendimento ao Cliente) ou em telas de Movimentação Financeira, verifique se existe o parâmetro **APRES.TGFPAR**. Caso não exista, crie-o em Configurações » Avançado » Preferências:

- Chave: `APRES.TGFPAR`
- Descrição: Apres. Razão Social nas Centrais e Mov. Financeira
- Módulo: Configurações
- Aba: Diversas (Tipo Texto)
- Texto: `RAZAOSOCIAL`

**(3)** Reinicie o servidor de aplicação (ou solicite a atualização do cache de parâmetros) para que as alterações sejam recarregadas.

**(4)** Acesse novamente as telas afetadas e confirme se a Razão Social passou a ser exibida.

**CAUSA**

Existem dois mecanismos independentes que controlam a exibição de Nome Fantasia x Razão Social do parceiro, e cada um afeta um conjunto diferente de telas:

- **NOMERAZAOPARC**: preferência de sistema (armazenada em cache) que controla o Portal de Vendas/Compras (Gerente On-line), sequência de visita, rota de entrega, dashboards comerciais/financeiros, emissão de cheques e notas de contingência.
- **APRES.TGFPAR**: chave dinâmica que define o Campo de Apresentação do Parceiro para as Centrais (ex.: Central de Liberações, Central de Atendimento ao Cliente) e para telas de Movimentação Financeira como parcelamento/renegociação.

O problema ocorre quando apenas um dos dois é configurado, ou quando o sistema não é reiniciado após a alteração, como ambos ficam em cache, a mudança só é aplicada após reinicialização do servidor (ou atualização do cache de parâmetros).
