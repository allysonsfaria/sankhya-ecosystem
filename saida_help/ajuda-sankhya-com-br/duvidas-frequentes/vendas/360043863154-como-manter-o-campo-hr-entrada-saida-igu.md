---
id: "360043863154"
titulo: "Como manter o campo Hr. entrada/saída igual a hora de confirmação da nota?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043863154-Como-manter-o-campo-Hr-entrada-sa%C3%ADda-igual-a-hora-de-confirma%C3%A7%C3%A3o-da-nota"
trilha: "Dúvidas Frequentes > Vendas"
atualizado_em: "2026-07-22T15:58:43Z"
rotulos: ["Configuração", "NF-e", "XML", "SEFAZ", "DANFE", "Preferências", "Ative \"SUBSTHRENTSAI\"", "Hora atual automática", "Restrição na emissão"]
---

# Como manter o campo Hr. entrada/saída igual a hora de confirmação da nota?

É possível substituir a hora de entrada/saída inserida no lançamento pela hora atual. Para tal, siga as orientações abaixo:

![Imagem 1: Acesse a tela "Preferências" (Caminho de acesso: Configurações » Avançado).](https://ajuda.sankhya.com.br/hc/article_attachments/17154664266135) Acesse a tela **"Preferências"** (Caminho de acesso: Configurações » Avançado).

Chave **"SUBSTHRENTSAI - Substitui hora de Entrada/Saída pela atual?":** ligado

![Imagem 2: Chave " SUBSTHRENTSAI - Substitui hora de Entrada/Saída pela atual?": ligado](https://ajuda.sankhya.com.br/hc/article_attachments/13162936997527)

- Se este parâmetro estiver configurado como 'Sim', que é o default, na impressão do Danfe o campo Hora de Saída será impresso com a hora da confirmação da nota;
- Mesmo que o usuário tente alterar o horário de entrada/saída do cabeçalho da nota, o sistema altera automaticamente para a data da confirmação;
- Quando o parâmetro estiver configurado para 'Não', o sistema irá permitir que o usuário informe manualmente o campo Hora Entrada/Saída do cabeçalho da nota e, ao confirmar a nota, essa hora não será alterada, imprimindo no DANFE a hora de Saída informada pelo usuário e não a hora da confirmação da nota.

![Imagem 3: IMPORTANTE:](https://ajuda.sankhya.com.br/hc/article_attachments/17154713372183) **IMPORTANTE:**

Atualmente o sistema não suporta que a data/hora de emissão da nota informada pelo usuário seja menor que a data/hora atual do servidor da SEFAZ. Portanto, as regras de negócio referentes aos parâmetros **"SUBSTHRENTSAI"** e **"IMPHRSAIDADANFE"** documentadas não se aplicam nesse contexto.

Além disso, o sistema está gerando no XML a tag "dhSaiEnt" igual a "dhEmi", para assim não gerar a rejeição de código 506: "Data de Saída menor que a Data de Emissão". Pois, o sistema não está preparado para permitir que o usuário informe a hora da tag "dhEmi" manualmente igual é realizado para a tag "dhSaiEnt"."
