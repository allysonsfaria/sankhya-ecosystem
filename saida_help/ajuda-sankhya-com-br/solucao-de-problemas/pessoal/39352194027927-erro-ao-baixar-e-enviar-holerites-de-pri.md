---
id: "39352194027927"
titulo: "Erro ao baixar e enviar holerites de primeira parcela e 2ª décimo terceiro salário"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39352194027927-Erro-ao-baixar-e-enviar-holerites-de-primeira-parcela-e-2%C2%AA-d%C3%A9cimo-terceiro-sal%C3%A1rio"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-07-29T13:22:51Z"
rotulos: ["Configuração", "Relatórios", "Preferências", "Folha", "Gerenciador de Folhas", "Erro", "Artigo criado KCS", "Sankhya RH - KCS"]
---

# Erro ao baixar e enviar holerites de primeira parcela e 2ª décimo terceiro salário

**MENSAGEM**

Falha. Não foi possível fazer o download. Motivo: Unable to get value for field 'FPRELATHOLDECIM' of class 'java.awt.Image'

**SITUAÇÃO**

Ao tentar **"baixar ou enviar por e-mail"** os holerites referentes à primeira parcela e segunda parcela do décimo terceiro salário, o sistema apresenta erro e não permite a conclusão da operação. O problema ocorre durante a geração do relatório de holerite do décimo terceiro.

**SOLUÇÃO**

Para corrigir o erro, siga os passos abaixo:

**(1)** Acesse a tela **"Parâmetros"** (Configurações » Avançado » Preferências).

**(2)** Localize o parâmetro **"Relatório Holerite Décimo Terceiro"** (FPRELATHOLDECIM).

![Imagem 1: Verifique se o campo (FPRELATHOLDECIM) está preenchido com algum código de relatório personalizado. Limpe o conteúdo do…](https://ajuda.sankhya.com.br/hc/article_attachments/41357173258135)
**(3)** Verifique se o campo (FPRELATHOLDECIM) está preenchido com algum código de relatório personalizado.
**(4)** Limpe o conteúdo do parâmetro, deixando-o NULL (vazio). Isso fará com que o sistema considere o relatório padrão da fonte do sistema.

![Imagem 2: (3) Verifique se o campo (FPRELATHOLDECIM) está preenchido com algum código de relatório personalizado. (4) Limpe o…](https://ajuda.sankhya.com.br/hc/article_attachments/41357143371415)![Imagem 3: (3) Verifique se o campo (FPRELATHOLDECIM) está preenchido com algum código de relatório personalizado. (4) Limpe o…](https://ajuda.sankhya.com.br/hc/article_attachments/41357173262359)

**(5)** Salve as alterações realizadas no parâmetro.

### Como medida complementar, verifique também o caminho da pasta padrão de relatórios:

- Ainda na tela **Preferências**, localize o parâmetro **"FPPASTAPADRAO"** (Caminho da pasta padrão de relatórios folha)
- Verifique se o caminho está correto e acessível

**Para capturar o caminho correto:**

- Acesse **Configurações » Avançado » Administração do Servidor**
- Localize o campo **"JAVA HOME"**
- Copie o caminho até o nome "java"
- Retorne às Preferências e cole o caminho no parâmetro **FPPASTAPADRAO**

**Formato esperado:**

- **Windows**: `C:\suapasta\sankhya-om\jboss\bin\`
- **Linux**: `/home/suapasta/relatorios/`

**(6)** Acesse novamente a tela de (Pessoal+ » Rotinas Folha » Gerenciador de Folhas) e realize uma nova geração do relatório.

**(7)** Tente realizar o **"download ou envio por e-mail"** dos holerites. O erro não deverá mais ocorrer.

**CAUSA**

O erro ocorre porque o parâmetro (FPRELATHOLDECIM) estava configurado com um código de relatório personalizado que não está disponível ou apresenta incompatibilidade. Quando o parâmetro está preenchido incorretamente, o sistema não consegue localizar ou processar o relatório especificado, gerando falha no download e envio dos holerites do décimo terceiro salário.
