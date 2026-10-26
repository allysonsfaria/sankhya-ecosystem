---
id: "42950652943639"
titulo: "Divergência de Casas Decimais (Quantidade, Desconto ou Preço)"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42950652943639-Diverg%C3%AAncia-de-Casas-Decimais-Quantidade-Desconto-ou-Pre%C3%A7o"
trilha: "VIDYA: Vendas externas, televendas e entregas > Central de ajuda > Produtos"
atualizado_em: "2026-08-24T16:08:46Z"
rotulos: ["sync_hc", "vidya", "vidya_593598", "sync_hash_4dfe2044fe33"]
---

# Divergência de Casas Decimais (Quantidade, Desconto ou Preço)

📌 **Sintoma do Erro**
Durante a digitação ou fechamento de um pedido, os campos numéricos de **quantidade**, **desconto** ou **preço** exibem uma formatação com mais ou menos casas decimais do que o modelo de negócio da empresa exige (ex: o sistema aceita frações como 1,50 para itens que só deveriam ser vendidos em unidades inteiras).

👀 **O que você vê nas Interfaces**

| **Ambiente / Módulo** | **Elementos e Alertas Exibidos na Tela** |
| --- | --- |
| **Carrinho de Compras / Inserção** | Presença de zeros à direita desnecessários ou permissão de inserção de valores fracionados em campos que deveriam ser travados como inteiros. |

🕵️‍♂️ **Causas Mais Comuns**

- **Dessincronização de Diretrizes:** O parâmetro de controle de decimais foi modificado no servidor administrativo, mas o aplicativo de campo do vendedor ainda não assimilou a nova regra.
- **Defasagem de Versão:** O smartphone está rodando uma versão antiga do aplicativo (frontend) que não possui suporte ao ajuste de precisão decimal configurado no backend.
- **Acúmulo de Cache:** Arquivos temporários locais forçando o comportamento de arredondamento antigo do smartphone.

🛠 **Como Corrigir o Problema**

1. **Ajuste de Parâmetro Master:** Acesse o painel administrativo web do Vidya Force e verifique o status do parâmetro **"Usa decimal para quantidade"** (ou similar), ligando-o ou desligando-o conforme a necessidade comercial.
2. **Reinicialização Forçada:** Peça para o vendedor fechar completamente o aplicativo (remover da lista de apps suspensos) e abri-lo novamente **com internet ativa** para forçar a sincronização da nova regra.
3. **Expurgar Cache Local:** Se persistir, acesse o menu interno do app, vá em **Configurações → Limpar dados locais**, refaça o login e aguarde o download completo da base.
4. **Update de Aplicativo:** Acesse a Google Play Store ou App Store e certifique-se de atualizar o Vidya Force para a última versão disponível.

💡 **Quando abrir chamado para a VidyaCode**

- Se o parâmetro web estiver correto, o aplicativo atualizado e limpo, mas os campos continuarem ignorando as travas de casas decimais.
- Caso a correção funcione normalmente em alguns smartphones da equipe, mas falhe em modelos específicos.
- Se houver a necessidade de implementar ou customizar um formato de parâmetro decimal que não esteja disponível no painel administrativo padrão.
