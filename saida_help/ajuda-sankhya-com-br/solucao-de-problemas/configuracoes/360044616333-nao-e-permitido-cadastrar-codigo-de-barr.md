---
id: "360044616333"
titulo: "Não é permitido cadastrar código de barras iniciado em 2 que case com a formatação de código de barras (parâmetro FORMABARRASQTD) juntamente com o parâmetro CODBARDECOMP2 ligado"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044616333-N%C3%A3o-%C3%A9-permitido-cadastrar-c%C3%B3digo-de-barras-iniciado-em-2-que-case-com-a-formata%C3%A7%C3%A3o-de-c%C3%B3digo-de-barras-par%C3%A2metro-FORMABARRASQTD-juntamente-com-o-par%C3%A2metro-CODBARDECOMP2-ligado"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-08-25T14:38:43Z"
rotulos: ["#criadoRoger", "CORE_E03947", "#RevisadoWellington", "Produtos", "Configuração", "CODBARDECOMP2", "Restrição no Cadastro de Código de Barras Iniciado em 2", "Erro", "FORMABARRASQTD"]
---

# Não é permitido cadastrar código de barras iniciado em 2 que case com a formatação de código de barras (parâmetro FORMABARRASQTD) juntamente com o parâmetro CODBARDECOMP2 ligado

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/18605650937111) MENSAGEM:**

[CORE\_E03947] Não é permitido cadastrar código de barras iniciado em 2 que case com a formatação de código de barras (parâmetro FORMABARRASQTD) juntamente com o parâmetro CODBARDECOMP2 ligado.

**![Imagem 2: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/18605650948631) CAUSA:**

Ocorre quando o parâmetro **Formatação código de barras - FORMABARRASQTD** está configurado  e **Cód.barras = Cód.Prod./Preço/Qtd, qdo iniciado c/2 - CODBARDECOMP2** está ligado, havendo um conflito de configuração.

**![Imagem 3: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18605650942871) SOLUÇÃO:**

Considere o Comportamento da aplicação, conforme abaixo:

![Imagem 4: Configurações » Avançado » Preferências](https://ajuda.sankhya.com.br/hc/article_attachments/18605650950807) Configurações » Avançado » Preferências

Pesquise pelos parâmetros:

- **Formatação código de barras - FORMABARRASQTD** = [Caso este esteja configurado]
- **Cód.barras = Cód.Prod./Preço/Qtd, qdo iniciado c/2 - CODBARDECOMP2** = [Quando ligado, o código de barras, quando iniciado com 2, vem do uso de Balança.]
- **Cód.barras = Cód.Prod./Preço/Qtd, qdo iniciado c/2 - CODBARDECOMP2** - Ligado entende que o todo código de barras começado em 2 são originado de balança, composto pela seguinte sintaxe "Cód.Prod./Preço/Qtd". Isso ocorre pois com o parâmetro ligado o sistema entende que esse produto foi pesado em balança e vendido de acordo com seu peso.

![Imagem 5: Importante revisar, pois caso algum produto realmente use a pesagem, não poderá desligar o parâmetro Cód.barras =…](https://ajuda.sankhya.com.br/hc/article_attachments/18605650953239)Importante revisar, pois caso algum produto realmente use a pesagem, não poderá desligar o parâmetro **Cód.barras = Cód.Prod./Preço/Qtd, qdo iniciado c/2 - CODBARDECOMP2**, então deverá ajustar as configurações de formação do parâmetro **Formatação código de barras - FORMABARRASQTD**.
