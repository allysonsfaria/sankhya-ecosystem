---
id: "360044616053"
titulo: "Não foi possível encontrar o arquivo de modelo 'Repo://pasta/nomearquivo.txt' no Repositório de Arquivos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044616053-N%C3%A3o-foi-poss%C3%ADvel-encontrar-o-arquivo-de-modelo-Repo-pasta-nomearquivo-txt-no-Reposit%C3%B3rio-de-Arquivos"
trilha: "Solução de Problemas > Configurações"
atualizado_em: "2026-07-22T15:54:29Z"
rotulos: ["#criadoRoger", "#Revisadoclaudio", "CORE_E02118", "Configuração", "Repositório de Arquivos", "Impressão", "NF-e", "Arquivo de Modelo Ausente no Repositório", "Erro"]
---

# Não foi possível encontrar o arquivo de modelo 'Repo://pasta/nomearquivo.txt' no Repositório de Arquivos

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/18788890012823) MENSAGEM:**

[CORE\_E02118] Não foi possível encontrar o arquivo de modelo 'Repo://pasta/nomearquivo.txt' no Repositório de Arquivos.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/18788864940695) SOLUÇÃO:**

![Imagem 3: Verifique na mensagem apresentada, qual é o modelo de impressão que está sendo validado.](https://ajuda.sankhya.com.br/hc/article_attachments/18788864949527) Verifique na mensagem apresentada, qual é o modelo de impressão que está sendo validado.

- **Exemplo:** Não foi possível encontrar o arquivo de modelo 'Repo://modelos/**DadosAdicionais.txt'** no Repositório de Arquivos.

Para o caso acima, o sistema reporta que não localizou o modelo "DadosAdicionais" no caminho setado para o mesmo.  Dessa forma, através das configurações de 'Modelo de dados Adicionais' seguir com as análises:

- Tela 'Tipos de Operação - TOP' >> Aba NF-e/NFC-e >> Campo '**Modelo para Dados Adicionais de NF-e**'.
- Localizar o modelo acima na tela **'Modelos de nota fiscal/duplicata/boleto'** e verificar o campo 'Caminho' informado para o respectivo modelo.
- Acessar a tela 'Repositório de Arquivos' e certificar-se que no caminho mencionado no item anterior está salvo o modelo com exatamente a mesma descrição mencionada na rejeição.
- Em caso negativo, sintonizar com o implantador da empresa, responsável pela configuração de tais modelos de impressão, de forma que esse seja inserido no caminho citado.

![Imagem 4: Se no campo Modelo de boleto (e-mail): estiver referenciando um caminho e um arquivo.](https://ajuda.sankhya.com.br/hc/article_attachments/18788890040855) Se no campo **Modelo de boleto (e-mail):**estiver referenciando um caminho e um arquivo.

- Acessar a tela 'Empresa' (Comercial/Preferências) >> Aba 'Boleto' >> 'Modelo de Boleto' : Verificar o caminho configurado.
- Acessar 'Configurações » Avançado » Repositório de Arquivos' e certificar-se que no caminho configurado no item anterior, existe um arquivo com exatamente a mesma descrição configurada nas preferências da empresa.
- Caso não esteja devidamente configurado, deverá solicitar ao implantador que tome as providencias para o ajuste, retirando o caminho no campo do 'Modelo de Boleto' >> Tela 'Empresa' (Comercial/Preferências) >> Aba 'Boleto'  ou criando e inserindo o modelo no Repositório de arquivos com exatamente a mesma descrição

**![Imagem 5: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/18788864956823) CAUSA:**

Ocorre quando foi configurado para o lançamento um caminho para localizar o respectivo modelo de impressão a ser utilizado, e esse modelo não está inserido no caminho.

**Observação**:

Parâmetro: **"Diretório base para o repositório de arquivos - FREPBASEFOLDER".**

Este parâmetro determina a pasta 'raiz', onde no servidor de aplicação sera armazenados os arquivos inseridos através da rotina Repositório de Arquivos- Recomenda-se cautela e conhecimento para efetuar qualquer ajuste neste parâmetro. Necessário comunicar a equipe de TI para efetuar qualquer manutenção no parâmetro.
