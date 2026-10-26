---
id: "7889042780439"
titulo: "Erro 174 - A data de ocorrência do evento xxxxxx deve ser igual ou posterior ao início da obrigatoriedade deste evento xxxxx para o empregador ao eSocial. Como resolver?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/7889042780439-Erro-174-A-data-de-ocorr%C3%AAncia-do-evento-xxxxxx-deve-ser-igual-ou-posterior-ao-in%C3%ADcio-da-obrigatoriedade-deste-evento-xxxxx-para-o-empregador-ao-eSocial-Como-resolver"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-07-29T13:24:22Z"
rotulos: ["Configuração", "Eventos", "Fiscal", "não apagar", "eSocial", "Erro 174", "Central do eSocial", "Datas Conflitantes", "Ajuste de Eventos", "Verificar Admissões", "Erro"]
---

# Erro 174 - A data de ocorrência do evento xxxxxx deve ser igual ou posterior ao início da obrigatoriedade deste evento xxxxx para o empregador ao eSocial. Como resolver?

**![Imagem 1: MENSAGEM :](https://ajuda.sankhya.com.br/hc/article_attachments/16542173175191) MENSAGEM**:

Erro 174 - A data de ocorrência do evento xxxxxx deve ser igual ou posterior ao início da obrigatoriedade deste evento xxxxx para o empregador ao eSocial. Para confirmar a data de obrigatoriedade do empregador, verifique o cronograma disponível no site https://portal.esocial.gov.br/.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16542173179415) SOLUÇÃO:**

Essa mensagem de erro pode ocorrer nas seguintes situações:

**![Imagem 3: Ao enviar o evento de cadastro inicial (S-2200 / S-2300).](https://ajuda.sankhya.com.br/hc/article_attachments/16542173181207) Ao enviar o evento de cadastro inicial (S-2200 / S-2300).**

Verifique se no cadastro do colaborador está marcada a opção **"Cad. inicial (eSocial)".**

**Opções:**

**- Sim:** para admissões anteriores a data de início do eSocial para esta empresa;

**- Não:** para admissões posteriores a data de início do eSocial para esta empresa;

**- Automático:** o sistema leva a informação de acordo a data de início do eSocial.

**![Imagem 4: Evento sendo gerado com data de alteração anterior a obrigatoriedade do esocial.](https://ajuda.sankhya.com.br/hc/article_attachments/16542173183255) Evento sendo gerado com data de alteração anterior a obrigatoriedade do esocial.**

**Exemplo:** S-2206 gerando com data 2019, porém o início da obrigatoriedade dessa empresa foi em 2020. Nesse caso, ajuste para uma data posterior a obrigatoriedade para que o evento seja enviado.

Para realizar esse ajuste, entre em contato com o service desk.

Se o envio do evento não for devido, pois a data dele é realmente antes da obrigatoriedade, entre em contato com service desk para verificar o motivo da geração indevida.

![Imagem 5: Se o envio do evento não for devido, pois a data dele é realmente antes da obrigatoriedade, entre em contato com…](https://ajuda.sankhya.com.br/hc/article_attachments/7893669818007)

**![Imagem 6: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16542144326295) CAUSA:**

O erro ocorre quando se tenta enviar um evento referente a uma fase no eSocial no qual a empresa ainda não está na obrigatoriedade.
