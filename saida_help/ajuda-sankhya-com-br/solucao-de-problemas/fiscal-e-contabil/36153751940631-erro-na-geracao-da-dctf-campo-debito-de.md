---
id: "36153751940631"
titulo: "Erro na Geração da DCTF: Campo “Débito de SCP/INC” Não Configurado"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/36153751940631-Erro-na-Gera%C3%A7%C3%A3o-da-DCTF-Campo-D%C3%A9bito-de-SCP-INC-N%C3%A3o-Configurado"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-07-22T14:23:33Z"
rotulos: ["Configuração", "Receita Federal", "Impostos", "Financeiro", "DCTF", "Débito de SCP/INC", "SCP", "Erro na Geração do Arquivo DCTF", "INC"]
---

# Erro na Geração da DCTF: Campo “Débito de SCP/INC” Não Configurado

**SITUAÇÃO:**

Ao gerar o arquivo da **DCTF**, o sistema apresentou erro relacionado à falta de configuração do campo **“Débito de SCP/INC”**.

Esse campo é obrigatório e deve ser corretamente definido para que o arquivo seja validado conforme as regras do guia oficial da DCTF.

##### SOLUÇÃO:

**(1)** Acesse a tela de [**''Geração do Arquivo DCTF''**](https://ajuda.sankhya.com.br/hc/pt-br/articles/6594908066583-Gera%C3%A7%C3%A3o-do-Arquivo-DCTF) (Livros Fiscais » Conexão » Geração do Arquivo DCTF).

**(2)** Na tela, selecione a aba ''**Configurações''** e, em seguida abra a sub-aba ''**Geral''**.

**(3)** Localize o campo **“Débito de SCP/INC”** e selecione a opção correspondente ao enquadramento da empresa:

- **INC** → quando a empresa for uma Incorporadora Imobiliária;
- **SCP** → quando a empresa for uma Sociedade em Conta de Participação;
- **Não é SCP nem INC** → para empresas que **não** se enquadram em nenhuma das categorias acima.

![Imagem 1: Não é SCP nem INC → para empresas que não se enquadram em nenhuma das categorias acima.](https://ajuda.sankhya.com.br/hc/article_attachments/36413843593367)

**(5)** Após ajustar o campo, clique em Salvar e gere novamente a Geração do Arquivo DCTF.

**(6)** Com a configuração correta aplicada, o arquivo DCTF será gerado com sucesso, conforme as validações exigidas pela Receita Federal.

**OBSERVAÇÃO:**

Antes de realizar essa configuração, **recomenda-se validar com o setor fiscal ou contábil qual opção é adequada ao enquadramento da empresa**, garantindo que a geração e o envio da DCTF ocorram corretamente.

##### CAUSA:

O erro ocorre quando o campo **“Débito de SCP/INC”** não está configurado na tela de Geração do Arquivo DCTF, na aba **''Configurações''** e sub-aba **''Geral''**.
