---
id: "360051071554"
titulo: "Navegador Sankhya não é iniciado - Tela \"branca\""
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360051071554-Navegador-Sankhya-n%C3%A3o-%C3%A9-iniciado-Tela-branca"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:30:15Z"
rotulos: ["Configuração", "Atualização", "--disable-gpu ", "placa grafica", "placa de video", "Navegador", "Corrigindo Tela em Branco no Navegador Sankhya", "Erro", "Navegador Sankhya", "Windows"]
---

# Navegador Sankhya não é iniciado - Tela "branca"

**![Imagem 1: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/18584750122519) CAUSA:**

Quando possuir Sistema Operacional Windows 7, ao atualizar o Navegador Sankhya, o mesmo pode apresentar tela em branco. A causa desse erro pode estar relacionado ao hardware (ex:placa gráfica da máquina).

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18584782550551) SOLUÇÃO:**

![Imagem 3: Executar o Navegador Sankhya através do 'Windows PowerShell', conforme .gif abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/18584782557335) Executar o Navegador Sankhya através do 'Windows PowerShell', conforme .gif abaixo:

[GIF animado: Imagem 4: Executar o Navegador Sankhya através do 'Windows PowerShell', conforme .gif abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/360079594014)

Verificar se foi apresentado erro, conforme imagem abaixo:

![Imagem 5: Verificar se foi apresentado erro, conforme imagem abaixo:](https://ajuda.sankhya.com.br/hc/article_attachments/360079594054)

Nesse caso, uma forma de corrigir o problema será:

![Imagem 6: Localizar o atalho do Navegador Sankhya e com o botão direito, localizar a opção 'Propriedades >> Destino', adicionar a…](https://ajuda.sankhya.com.br/hc/article_attachments/18584750147991) Localizar o atalho do Navegador Sankhya e com o botão direito, localizar a opção 'Propriedades >> **Destino',** adicionar a informação abaixo:

**--disable-gpu**

**Exemplo: "C:\SANKHYA\Navegador Sankhya\NavegadorSankhya.exe" --disable-gpu**

Veja em detalhes:

[GIF animado: Imagem 7: Veja em detalhes:](https://ajuda.sankhya.com.br/hc/article_attachments/360079594234)

![Imagem 8: Feito isso, tente abrir o navegador novamente.](https://ajuda.sankhya.com.br/hc/article_attachments/18584750153111) Feito isso, tente abrir o navegador novamente.
