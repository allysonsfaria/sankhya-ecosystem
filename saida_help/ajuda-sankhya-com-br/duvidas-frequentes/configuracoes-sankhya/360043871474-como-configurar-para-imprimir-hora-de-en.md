---
id: "360043871474"
titulo: "Como configurar para imprimir Hora de Entrada/Saída (HRENTSAI) na Impressão do DANFE?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043871474-Como-configurar-para-imprimir-Hora-de-Entrada-Sa%C3%ADda-HRENTSAI-na-Impress%C3%A3o-do-DANFE"
trilha: "Dúvidas Frequentes > Configurações Sankhya"
atualizado_em: "2026-07-22T15:58:04Z"
rotulos: ["Configuração", "Impressão", "NF-e", "DANFE", "TOP", "Parâmetros", "Configuração da Impressão do DANFE com Hora de Entrada/Saída"]
---

# Como configurar para imprimir Hora de Entrada/Saída (HRENTSAI) na Impressão do DANFE?

![Imagem 1: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/17151647919255) **SOLUÇÃO:**

O sistema permite a alteração/digitação da **Hr. Ent./Saida** para o DANFE, quando o documento for do Tipo (V-Venda, D-Devolução de Venda, E-Devolução de Compra, T-Transferência).

- Existe o parâmetro "**SUBSTHRENTSAI - Substitui hora de Entrada/Saída pela atual?**"

![Imagem 2: Quando o parâmetro estiver ligado , na impressão do DANFE o campo 'Hr. Ent./Saida' (HRENTSAI) será impresso com a hora…](https://ajuda.sankhya.com.br/hc/article_attachments/17151632061335) Quando o parâmetro estiver **ligado**, na impressão do DANFE o campo 'Hr. Ent./Saida' (HRENTSAI) será impresso com a hora da confirmação da nota, mesmo que o usuário tenha alterado a hora no campo, o sistema buscará a hora da confirmação da nota e gravará no campo: **"Horário do servidor de Aplicação"**.

![Imagem 3: Quando o parâmetro estiver deligado , o sistema irá permitir que o usuário informe manualmente o campo "Hr. Ent./Saida"…](https://ajuda.sankhya.com.br/hc/article_attachments/17151632066327) Quando o parâmetro estiver **deligado**, o sistema irá permitir que o usuário informe manualmente o campo **"Hr. Ent./Saida"** do cabeçalho da nota e, ao confirmar a nota, essa hora não será alterada.
Caso o campo **Hr. Ent./Saida** esteja em branco, continuará em branco, após a confirmação.

**![Imagem 4: IMPORTANTE:](https://ajuda.sankhya.com.br/hc/article_attachments/17151647931031) IMPORTANTE:**

**(1)** Atualmente o sistema não suporta que a data/hora de emissão da nota informada pelo usuário seja menor que a data/hora atual do servidor da SEFAZ. Portanto, as regras de negócio referentes aos parâmetros **"SUBSTHRENTSAI"** e **"IMPHRSAIDADANFE"** documentadas não se aplicam nesse contexto.

**(1)** Além disso, o sistema está gerando no XML a tag "dhSaiEnt" igual a "dhEmi", para assim não gerar a rejeição de código 506: "Data de Saída menor que a Data de Emissão" pois, o sistema não está preparado para permitir que o usuário informe a hora da tag "dhEmi" manualmente igual é realizado para a tag "dhSaiEnt"."

**![Imagem 5: OBSERVAÇÕES:](https://ajuda.sankhya.com.br/hc/article_attachments/17151647938839) OBSERVAÇÕES:**

A marcação no cadastro da TOP (Caminho de acesso: Comercial » Arquivo » Cadastros » Tipos de Operação - TOP, aba: Validações) é soberana ao parâmetro IMPHRSAIDADANFE, ou seja:

**(1)** Caso o parâmetro IMPHRSAIDADANFE esteja ligado e o campo da TOP **"Imprimir NF-e sem Data de Entrada/Saída:"** esteja marcado, na impressão do DANFE os campos Data da Entrada/Saída e Hora da Saída, ficarão em branco.

(2)**Configurações:**

![Imagem 6: Acesse: Comercial » Arquivo » Cadastros » Tipos de Operação - TOP , aba: Validações](https://ajuda.sankhya.com.br/hc/article_attachments/17151632061335) Acesse: Comercial » Arquivo » Cadastros » Tipos de Operação - TOP, aba: Validações

![Imagem 7: Acesse: Comercial » Arquivo » Cadastros » Tipos de Operação - TOP , aba: Validações](https://ajuda.sankhya.com.br/hc/article_attachments/13170560816663)

![Imagem 8: Configurações » Avançado » Preferências](https://ajuda.sankhya.com.br/hc/article_attachments/17151632066327) Configurações » Avançado » Preferências

**(1)** Parâmetros:

- **"SUBSTHRENTSAI - Substitui hora de Entrada/Saída pela atual?"**
- **"IMPHRSAIDADANFE-Imprimir hora de saída na impressão no DANFE"**
