---
id: "360047200574"
titulo: "Como configurar a geração da 'Inscrição Estadual do Substituto tributário' no XML ? [Tag <IEST>]"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360047200574-Como-configurar-a-gera%C3%A7%C3%A3o-da-Inscri%C3%A7%C3%A3o-Estadual-do-Substituto-tribut%C3%A1rio-no-XML-Tag-IEST"
trilha: "Dúvidas Frequentes > Vendas"
atualizado_em: "2026-07-22T15:32:02Z"
rotulos: ["Configuração", "NF-e", "XML", "SEFAZ", "Impostos", "Marcar \"Gerar GNRE?\" ICMS-ST na NF-e", "Inscrição Estadual do Substituto tributário", "Informar UF no parâmetro UFIESTDIFAL", "IEST"]
---

# Como configurar a geração da 'Inscrição Estadual do Substituto tributário' no XML ? [Tag <IEST>]

Utilize essa funcionalidade com responsabilidade e autorização de seu Contador, quando a própria SEFAZ exigir a Insc. Estadual de Substituto Tributário para NF-e com cálculo do DIFAL.

**(1)** Acesse a tela 'Preferências' (Configurações » Avançado » Preferências):

- Informe no parâmetro **UFIESTDIFAL** [UFs com Inscrição Estadual para Difal], a UF que existe a necessidade de informar a IE do Substituto, conforme exemplo abaixo:

![Imagem 1: Informe no parâmetro UFIESTDIFAL (UFs com Inscrição Estadual para Difal), a UF que existe a necessidade de informar a…](https://ajuda.sankhya.com.br/hc/article_attachments/14704800908183)

**(2)** Acesse a tela 'Empresa' (Comercial » Preferências » Empresa)
**Aba** 'Insc. Estadual Contribuinte ST no Estado Dest.' informar a UF e a IE:

![Imagem 2: (2) Acesse a tela 'Empresa' (Comercial » Preferências » Empresa) Aba 'Insc. Estadual Contribuinte ST no Estado Dest.'…](https://ajuda.sankhya.com.br/hc/article_attachments/14704817335575)

- Deve-se informar nesta aba, a Unidade Federativa (UF) e o número da Inscrição Estadual de Substituto Tributário das UFs onde a empresa tiver cadastrado Inscrição para recolhimento do ICMS-ST.

**Aba**: **"Livros Fiscais"**  desta rotina, deve-se marcar a opção **"Gerar GNRE?"** e na aba **"Insc. Estadual de Contribuinte ST no Estado Dest."**, cadastra-se a **"Inscrição da Empresa na UF de Destino"**.

**(3)** No [Cadastro de Tipos de Operações - TOP](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044603114-Tipos-de-Opera%C3%A7%C3%A3o-TOP) aba **"Financeiro"**, marcar o campo **"Gerar GNRE?"**.

**(4)** A Nota Fiscal tem que incidir ICMS-ST

Com essas configurações o sistema gera a tag IEST no XML da NF-e.
