---
id: "360044514193"
titulo: "Como parametrizar o sistema para deduzir o ICMS da base de cálculo do PIS e COFINS"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044514193-Como-parametrizar-o-sistema-para-deduzir-o-ICMS-da-base-de-c%C3%A1lculo-do-PIS-e-COFINS"
trilha: "Dúvidas Frequentes > Vendas"
atualizado_em: "2026-07-22T15:56:05Z"
rotulos: ["#criadoRoger", "CT-e", "Configuração", "NF-e", "COFINS", "PIS", "ICMS", "Impostos", "Configure ICMS/PIS-COFINS", "Opções nas preferências", "Ajuste em Tipos de Operação"]
---

# Como parametrizar o sistema para deduzir o ICMS da base de cálculo do PIS e COFINS

**(1)**  **Estas configurações são validadas somente para lançamentos efetuados nos portais**

![Imagem 1: Acesse a tela "Preferências" (Caminho de acesso: Configurações » Avançado).](https://ajuda.sankhya.com.br/hc/article_attachments/16647671407895) Acesse a tela **"Preferências"** (Caminho de acesso: Configurações » Avançado).

Chave **"REDICMSBCPISCOF** **- Redução do ICMS da BC do PIS e COFINS":** ligado

![Imagem 2: Acesse a tela "Empresa" (Caminho de acesso: Comercial » Preferências ).](https://ajuda.sankhya.com.br/hc/article_attachments/16647671410071) Acesse a tela **"Empresa"** (Caminho de acesso: Comercial » Preferências ).

Na aba **"Propriedades",** defina o campo**"Deduzir valor do ICMS na BC do PIS e COFINS?:"** conforme necessidade:

- **Não Deduz**: o valor do ICMS da base de cálculo do PIS/COFINS não será deduzido;
- **Deduz para CT-e:** ao realizar o lançamento de um CT-e, o valor do ICMS será deduzido da base de cálculo do PIS e COFINS; se as alíquotas de PIS e COFINS possuírem um percentual de redução de base, primeiramente será retirado o valor do ICMS da base, para depois ser aplicado o percentual de redução.
- **Deduz para CT-e e NF-e:** o valor do ICMS da base de cálculo do PIS/COFINS será deduzido tanto para NF-e quanto para CT-e;
- **Deduz para NF-e:**deduz o valor do ICMS da base de cálculo do PIS/COFINS apenas para NF-e.
- **Configurado pela Top**: esta opção verificará se a marcação **"Deduzir valor do ICMS na BC do PIS e COFINS?"** na tela [**"Tipos de Operação - TOP"**](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP#abaimpostos), aba **"Impostos"** encontra-se selecionada. Caso esteja habilitada esta marcação, ao efetuar um novo lançamento de nota, o sistema irá subtrair da Base de Cálculo de PIS/COFINS o valor referente ao cálculo de ICMS.

**![Imagem 3: IMPORTANTE:](https://ajuda.sankhya.com.br/hc/article_attachments/16647671404695) IMPORTANTE:**

O ICMS será deduzido da base de PIS/COFINS para lançamentos NF-e = Terceiros apenas quando o campo 'Deduzir valor do ICMS na BC do PIS e COFINS?' estiver configurado como 'Configurado pela TOP' e na TOP estiver marcado o campo 'Deduzir valor do ICMS na BC do PIS e COFINS?' aba Impostos.

Nos cenários em que se tem o cálculo do FCP (Fundo de Combate a Pobreza), o sistema não realiza a dedução do imposto da base do PIS/COFINS caso o campo NF-e no cadastro da TOP seja parametrizado como nota de terceiros. A dedução ocorre apenas em notas configuradas como normal, complementar, de ajuste e devolução.

![Imagem 4: Acesse: Comercial » Arquivo » Cadastros » Tipos de Operação - TOP , aba: Impostos .](https://ajuda.sankhya.com.br/hc/article_attachments/16647611518871) Acesse: Comercial » Arquivo » Cadastros » Tipos de Operação - TOP, aba: Impostos.

**"Deduzir valor do ICMS na BC do PIS e COFINS?"**: marque, caso a opção do Preferências da Empresa esteja selecionado, conforme indicado no item 2. Esta marcação é histórica, qualquer ajuste deverá lançar novo documento.

**![Imagem 5: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16647671415703) OBSERVAÇÃO:**

Caso o DIFAL tenha que ser deduzido da Base do PIS e COFINS, atente-se a configuração no cadastro da empresa.

![Imagem 6: Acesse a tela Empresa (Comercial » Preferências )](https://ajuda.sankhya.com.br/hc/article_attachments/16647671417495) Acesse a tela Empresa (Comercial » Preferências )

Marque **"Deduzir DIFAL"** junto com o ICMS na BC do PIS e COFINS

![Imagem 7: Marque " Deduzir DIFAL" junto com o ICMS na BC do PIS e COFINS](https://ajuda.sankhya.com.br/hc/article_attachments/14651633489047)
