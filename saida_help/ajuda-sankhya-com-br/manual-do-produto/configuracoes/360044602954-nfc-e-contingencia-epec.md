---
id: "360044602954"
titulo: "NFC-e - Contingência EPEC"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602954-NFC-e-Conting%C3%AAncia-EPEC"
trilha: "Manual do Produto > Configurações e Cadastros > Configurações"
atualizado_em: "2026-07-29T13:53:04Z"
rotulos: ["Configuração", "EPEC", "Fiscal", "SEFAZ", "Contingência", "NFC-e", "Off-Line", "Pendente de Retorno", "NFC-e - Contingência EPEC manual", "Contingência EPEC na Emissão de NFC-e", "Documentos Eletrônicos"]
---

# NFC-e - Contingência EPEC

A NFC-e é um processo que envolve diversos recursos de infraestrutura, hardware e software. Sendo assim o mau funcionamento ou indisponibilidade desses recursos, pode prejudicar o processo de autorização da NFC-e, com reflexos nos negócios do emissor da NFC-e, que fica impossibilitado de obter a prévia autorização de uso da NFC-e exigida pela legislação para a impressão do DANFE, que é necessário para acompanhar a circulação da mercadoria.

A contingência EPEC permite que a empresa solicite o registro do **"Evento Prévio de Emissão em Contingência"** anterior do documento em si, utilizando um leiaute mínimo de informações.

O envio de NFC-e para contingência EPEC, está disponível somente para o estado de São Paulo - SP.

Os principais benefícios deste tipo de contingência são:

- Reduzir custo da emissão em Formulário de Segurança (FS-DA);
- Conceder uma rota alternativa em caso de falha da infraestrutura de internet para acesso ao ambiente normal da SEFAZ Autorizadora;
- Geração de arquivo pequeno, com melhores condições de transmissão, em função de possíveis problemas de largura de banda e outras restrições na transmissão (uso de linha discada, rede celular etc);
- Garante o registro digital em sistema acessível pelo fisco do evento gerador de ICMS no momento em que ocorre.

Na imagem abaixo, tem-se a representação do fluxo de envio de uma NFC-e para contingência EPEC. A empresa emitente de NFC-e envia uma solicitação de consulta de Status de Serviço para verificar se o ambiente da SEFAZ autorizadora está disponível, se esta estiver indisponível, o fluxo a ser seguido deve ser, gerar um documento em EPEC e enviar para a SEFAZ autorizadora do EPEC.

![Imagem 1: Na imagem abaixo, tem-se a representação do fluxo de envio de uma NFC-e para contingência EPEC. A empresa emitente de…](https://ajuda.sankhya.com.br/hc/article_attachments/5021228893463)

Tem-se também a possibilidade de o ambiente da SEFAZ autorizadora do EPEC estar indisponível, neste caso, o processo a ser seguido, é o envio do documento para a contingência off-line ou SAT em alguns estados.

A emissão do EPEC poderá ser adotada por qualquer emissor (dentro do estado de São Paulo) que esteja impossibilitado de transmissão e/ou recepção das autorizações de uso de suas NFC-e, onde adota-se os seguintes passos:

**(1)** Gerar a NFC-e com "tpEmis = 4", mantendo também a informação do motivo de entrada em contingência com sua data e hora de início, com número diferente de qualquer NFC-e que tenha sido transmitida com outro "tpEmis";

**(1)** Gerar o arquivo XML do EPEC com as seguintes informações da NFC-e:

- UF, CNPJ e Inscrição Estadual do emitente;
- Chave de Acesso;
- UF e CNPJ ou CPF do destinatário se Valor Total da nota acima de R$10.000,00;
- Valor Total da NFC-e, Valor Total do ICMS;
- Outras informações constantes no leiaute.

**(1)** Assinar o arquivo com o certificado digital do emitente;

**(1)** Enviar o arquivo XML do EPEC para o Web Service de registro de eventos do ambiente de contingência da SEFAZ autorizadora;

**(1)** Impressão do DANFE da NFC-e que consta do EPEC, em papel comum, contendo no corpo a expressão "DANFE impresso em contingência – EPEC regularmente recebida pela SEFAZ autorizadora".

**(1)** Adotar as seguintes providências, após a resolução dos problemas técnicos que impediam a transmissão da NFC-e para o ambiente normal da SEFAZ autorizadora:

- Transmitir as NFC-e emitidas em Contingência Eletrônica para o ambiente normal da SEFAZ, observando o prazo limite de transmissão na legislação, bem como outros procedimentos constantes na legislação caso ocorram rejeições na autorização de uso;
- A Chave de Acesso desta NFC-e é a mesma Chave de Acesso do EPEC autorizado.

As notas devem ser configuradas para envio de NFC-e (configuração de NFC-e), porém na tela [Preferências da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa), aba [Sub-aba NF-e](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045114893-Prefer%C3%AAncias-da-Empresa#sub-abaNF-e), o campo **"Tipo de Envio NF-e"** deve ser definido com a opção **"SEFAZ/Contingência"** e o campo **"Envio em Contingência"** com a opção **"EPEC"**.

![Imagem 2: As notas devem ser configuradas para envio de NFC-e (configuração de NFC-e), porém na tela Preferências da Empresa ,…](https://ajuda.sankhya.com.br/hc/article_attachments/4962476314775)

Isso se faz necessário para que o sistema tente enviar a nota para a SEFAZ autorizadora e caso esta esteja indisponível, a nota seja enviada para uma contingência que está definida no campo.

A nota será enviada para ambiente de contingência EPEC, quando o servidor da SEFAZ autorizadora de NFC-e estiver indisponível. Nesse caso, o sistema verifica essa indisponibilidade e envia a nota para contingência EPEC.

Ao enviar a nota para EPEC, o sistema ficará com status de **"Enviada EPEC"** e com os dados de Data e Hora de Recebimento e Número de Recebimento preenchidos, isso significa que a nota foi enviada e autorizada no ambiente de contingência.

![Imagem 3: Ao enviar a nota para EPEC, o sistema ficará com status de "Enviada EPEC" e com os dados de Data e Hora de Recebimento…](https://ajuda.sankhya.com.br/hc/article_attachments/4962731916951)

As notas enviadas para EPEC, possuem um prazo limite para envio à SEFAZ autorizadora; caso as notas não sejam enviadas, o CNPJ será bloqueado para envio de notas para contingência até que todas as pendências sejam solucionadas (ou seja, até que todas as notas emitidas para EPEC sejam enviadas para a SEFAZ).

O processo descrito acima, é a maneira básica para envio de NFC-e para contingência EPEC.

O servidor de contingência EPEC, pode estar indisponível em alguns momentos para manutenção, ou até mesmo porque estes servidores só estarão disponíveis quando a SEFAZ autorizadora do EPEC identificar que existe um problema na SEFAZ autorizadora principal. Deste modo, pode acontecer uma certa demora na identificação e não será possível enviar a nota para a SEFAZ e nem para o EPEC; neste caso, o sistema assumirá o envio para **"Contingência Off-Line"** ou **"SAT"** (no caso do estado de São Paulo) realizando o envio diretamente para este ambiente.

Pode ser que ocorram alguns problemas durante o envio e não ser retornado o status da nota no servidor da SEFAZ autorizadora de EPEC; nesta situação, apenas é de conhecimento que a nota foi enviada, não se sabe se a mesma foi autorizada ou ocorreu algum erro.

Para contornar este cenário, tem-se duas opções no sistema, **"Marcar as notas como Contingência OFF-Line"** e **"Marcar as notas como Pendente de Retorno"** (localizado na grade [Resultado da seleção](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044601454-Portal-de-Vendas-Atributos-da-Tela#grade-resultadodaseleo) no botão **"NFC-e"**, da tela [Portal de Vendas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044612654)) que serão utilizadas para gerar uma nova nota que será cópia da nota original (a nota enviada para EPEC); da nota original, serão removidos todos os dados que são preenchidos no envio da nota, como Status, Data de Recebimento, entre outros (essa nota ficará disponível para outra operação de envio, para qualquer ambiente que aceite NFC-e SEFAZ, EPEC ou Contingência Off-Line).

A opção Marcar as notas como Pendente de Retorno, gera uma nova nota cópia da nota selecionada; esta ficará disponível até que o usuário saiba qual o status da mesma junto a SEFAZ autorizadora do EPEC; se a nota tiver sido autorizada (esta deve ser enviada para SEFAZ e posteriormente cancelada; caso tenha ocorrido algum erro, a nota dever ser removida do sistema para que não haja influência desta nas receitas e despesas da empresa); por meio desta opção, também é realizado o procedimento de limpar todos os dados que evidenciam que a nota original já tenha sido enviada para EPEC; assim, a nota ficará disponível para envio novamente para qualquer outro meio autorizador de EPEC; geralmente neste caso, a nota é enviada para contingência **"Off-Line"**.

![Imagem 4: A opção Marcar as notas como Pendente de Retorno , gera uma nova nota cópia da nota selecionada; esta ficará disponível…](https://ajuda.sankhya.com.br/hc/article_attachments/5012822945303)

[[Voltar ao topo]](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044602954-NFC-e-Conting%C3%AAncia-EPEC#top)
