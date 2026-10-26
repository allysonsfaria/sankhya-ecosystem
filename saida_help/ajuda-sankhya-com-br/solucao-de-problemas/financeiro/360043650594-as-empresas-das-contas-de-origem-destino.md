---
id: "360043650594"
titulo: "As empresas das contas de origem/destino devem ser iguais ou uma das contas não pode ser exclusiva"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043650594-As-empresas-das-contas-de-origem-destino-devem-ser-iguais-ou-uma-das-contas-n%C3%A3o-pode-ser-exclusiva"
trilha: "Solução de Problemas > Financeiro"
atualizado_em: "2026-08-22T19:15:44Z"
rotulos: ["#PUBLIFER", "CORE_E04083", "Configuração", "Contas", "Movimentação Financeira", "Financeiro", "Empresas iguais ou não exclusivas", "Ajuste de configurações", "Empresas diferentes e exclusividade", "Erro"]
---

# As empresas das contas de origem/destino devem ser iguais ou uma das contas não pode ser exclusiva

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16170334076183) MENSAGEM:**

[CORE\_E04083] As empresas das contas de origem/destino devem ser iguais ou uma das contas não pode ser exclusiva.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16170334082711) SOLUÇÃO:**

Quando o parâmetro **"Validar Empresa Exclusiva das Contas? - TRANSFMBEXC"** estiver habilitado, será permitido realizar a transferência e a conciliação entre contas exclusivas por meio de duas hipóteses:

- Se as empresas das contas de origem/destino forem iguais;
- Quando somente uma das contas for exclusiva.

![Imagem 3: Dessa forma, acesse o cadastro das contas utilizadas durante o processo de transferência e certifique-se que a situação…](https://ajuda.sankhya.com.br/hc/article_attachments/16170334090903) Dessa forma, acesse o cadastro das contas utilizadas durante o processo de transferência e certifique-se que a situação acima é respeitada:

Tela **"Contas"** (Caminho de acesso: Configurações » Cadastros » Bancários » Contas), aba **Cadastros**:

- Campo **"Empresa"**: Se a conta for para movimentação de empresa, informe o nome da empresa.
- Campo **'Exclusiva da Empresa':** Se esta opção for selecionada, a conta somente poderá ser utilizada pela empresa selecionada no campo acima. Ajuda a evitar lançamentos em contas erradas.

![Imagem 4: Campo 'Exclusiva da Empresa': Se esta opção for selecionada, a conta somente poderá ser utilizada pela empresa…](https://ajuda.sankhya.com.br/hc/article_attachments/14561226037015)

Se para as duas contas utilizadas, o campo **"Empresa"** for igual, a transferência será aceita.
Caso trate-se de empresas diferentes, uma delas não poderá ser exclusiva da empresa.

![Imagem 5: De acordo com as validações acima e processo atual da empresa, realize os devidos ajustes e refaça a transferência.](https://ajuda.sankhya.com.br/hc/article_attachments/16170334094487) De acordo com as validações acima e processo atual da empresa, realize os devidos ajustes e refaça a transferência.

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16170334100759) CAUSA:**

Quando as empresas das contas de origem/destino forem diferentes e ambas as contas forem "exclusivas da empresa", transferências entre essas contas não serão permitidas.
