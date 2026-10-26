---
id: "32396794581143"
titulo: "Documento XXXXX: No space Left on device"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/32396794581143-Documento-XXXXX-No-space-Left-on-device"
trilha: "Solução de Problemas > Vendas"
atualizado_em: "2026-07-22T14:31:32Z"
rotulos: ["Configuração", "Servidor", "Passos para resolver", "Razão do erro", "Detalhe do erro", "No space Left on device", "space", "left on device", "impressão de pdf", "documento no space", "espaço em disco", "erro de impressão", "Erro"]
---

# Documento XXXXX: No space Left on device

![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/32396781317271) **MENSAGEM:**

Documento XXXXX: No space Left on device.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/32396794571927)SOLUÇÃO:**

Libere **espaço em disco** no servidor onde o sistema está instalado.

**Recomendado:**

(1)** Acione o DBA ou administrador de infraestrutura**, que poderá:

**(1)** Verificar o volume afetado (geralmente `/tmp`, `/var`, `C:\Temp` ou diretórios específicos).

**(1)** Realizar a **limpeza de arquivos temporários antigos ou não utilizados**.

**(1)** Avaliar e, se possível, redimensionar o volume ou mover dados antigos para armazenamento externo.

**(2)** Caso a empresa **não tenha DBA, equipe de infraestrutura ou hospedagem de servidor** é recomendável acionar a unidade de negocio.

**![Imagem 3: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/32396794573079)CAUSA:**

Esse erro ocorre devido à **falta de espaço livre em disco no servidor de aplicação**.

No momento da geração do PDF (ou outro tipo de saída de impressão), o sistema Sankhya precisa alocar espaço em disco para criar arquivos temporários. Caso o volume de armazenamento onde esses arquivos são gravados esteja cheio, o sistema operacional retorna o erro `"No space left on device"`, impedindo a conclusão da tarefa.
