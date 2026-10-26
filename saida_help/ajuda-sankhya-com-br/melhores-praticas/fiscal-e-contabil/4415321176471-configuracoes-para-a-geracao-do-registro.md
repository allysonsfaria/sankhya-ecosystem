---
id: "4415321176471"
titulo: "Configurações para a geração do Registro F130 no arquivo EFD Contribuições"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/4415321176471-Configura%C3%A7%C3%B5es-para-a-gera%C3%A7%C3%A3o-do-Registro-F130-no-arquivo-EFD-Contribui%C3%A7%C3%B5es"
trilha: "Melhores Práticas > Fiscal e Contábil"
atualizado_em: "2026-07-22T15:20:19Z"
rotulos: ["Produtos", "Configuração", "Fiscal", "Impostos", "EFD Contribuições", "Configuração do F130: Marque na aba EFD", "Produtos: Desmarque créditos", "Detalhes Importantes: Configure tributos datas"]
---

# Configurações para a geração do Registro F130 no arquivo EFD Contribuições

Confira neste artigo as configurações para a geração do Registro **F130** (**Bens Incorporados ao Ativo Imobilizado – Operações Geradoras de Créditos com Base no Valor de Aquisição/Contribuição**) no arquivo **EFD Contribuições.**

**Passos:**

![Imagem 1: Na tela Comercial » Preferências » Empresa , aba " EFD - Escrituração Fiscal Digital " , selecione o tipo de…](https://ajuda.sankhya.com.br/hc/article_attachments/16250862016407) Na tela **Comercial » Preferências » Empresa**, aba **"EFD - Escrituração Fiscal Digital"**, selecione o tipo de escrituração **"EFD Contribuições"** e confira se o registro F130 está configurado para ser gerado:

![Imagem 2: Na tela Comercial » Preferências » Empresa , aba " EFD - Escrituração Fiscal Digital " , selecione o tipo de…](https://ajuda.sankhya.com.br/hc/article_attachments/15745357437079)

![Imagem 3: Acesse a tela "Produtos" ( Caminho de acesso: Configurações » Cadastros » Produtos ), aba "Impostos" e certifique se o…](https://ajuda.sankhya.com.br/hc/article_attachments/16250862018327) Acesse a tela **"Produtos"** (Caminho de acesso: Configurações » Cadastros » Produtos), aba **"Impostos"** e certifique se o flag **"Tem Créd. PIS/COFINS sobre Deprec. mensal"** está **desmarcado**.

**![Imagem 4: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16250889742999) OBSERVAÇÃO:**

 Este check box somente deverá estar marcado caso necessite gerar o registro F120.

![Imagem 5: Este check box somente deverá estar marcado caso necessite gerar o registro F120.](https://ajuda.sankhya.com.br/hc/article_attachments/15745419337111)

![Imagem 6: Ainda na tela ' Produtos ', acessar a aba ' Bens ', sub-aba ' Geral ' e configurar os campos abaixo para cada bem a ser…](https://ajuda.sankhya.com.br/hc/article_attachments/16250862021911) Ainda na tela '**Produtos**', acessar a aba '**Bens**', sub-aba '**Geral**' e configurar os campos abaixo para cada bem a ser considerado no registro F130:

-Cód.Sit.Tributária PIS:

-Cód.Sit.Tributária COFINS:

-Alíquota de PIS

-Alíquota de COFINS

-Nro. Parcelas Apr. Cred. PIS/COFINS: (Mesmo se for uma parcela) .

![Imagem 7: -Nro. Parcelas Apr. Cred. PIS/COFINS: (Mesmo se for uma parcela) .](https://ajuda.sankhya.com.br/hc/article_attachments/15745406069783)

**3.1** - O bem não pode ter data de baixa, mas se tiver, a data deve ser Superior a data de geração do EFD, assim estamos tratando de um período ainda acobertado pela compra.

**3.2** - A data da compra deve ser menor que a data de geração do EFD.

**3.3** - Deve ter algum valor no campo "Nro. Parcelas Apr. Cred. PIS/COFINS" no cadastro do bem.

OBS: Se estiver marcado a opção "Participa da MP540 PIS/COFINS", o sistema não vai pegar o que foi informado no referido campo, e vai fazer as seguintes validações:

Se a data de compra for menor que 03/08/2011, o sistema não vai apropriar nenhum valor de parcela para o crédito PIS/COFINS, outra situação é se a data de compra for igual ou maior que 01/07/2012, o sistema vai entender que o numero de parcelas é apenas 1, no entanto, se a data de compra não é menor que 03/08/2011 e não é maior ou igual a 01/07/2012, o sistema vai pegar como meses a apropriar, a diferença de meses entre a data 01/07/2012 e a data de compra informada para o bem.

-A data de geração deve estar acobertada pela quantidade de meses que foram informados no tópico 3 desse artigo, mais a data de compra, exemplo:

Data de compra = 01/01/2022

Meses encontrados no tópico 3 = 24

Até a data de geração do EFD Contribuições de 01/01/2024 o sistema vai gerar os valores de créditos no

F130 para o imobilizado.

![Imagem 8: Além das configurações citadas acima, se faz necessário também que o calculo da depreciação para este bem tenha sido…](https://ajuda.sankhya.com.br/hc/article_attachments/16250889746455) Além das configurações citadas acima, se faz necessário também que o calculo da depreciação para este bem tenha sido realizado ao menos em 1 mês.
