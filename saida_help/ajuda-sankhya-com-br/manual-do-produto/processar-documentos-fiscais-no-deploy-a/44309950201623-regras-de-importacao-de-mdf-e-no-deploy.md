---
id: "44309950201623"
titulo: "Regras de importação de MDF-e no Deploy Agent"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44309950201623-Regras-de-importa%C3%A7%C3%A3o-de-MDF-e-no-Deploy-Agent"
trilha: "Manual do Produto > Inteligência e Análise > Deploy Agent > Processar documentos fiscais no Deploy Agent"
atualizado_em: "2026-10-21T21:03:52Z"
---

# Regras de importação de MDF-e no Deploy Agent

## O que é e para que serve

Este artigo reúne as regras que o Deploy Agent aplica na importação.

A importação de MDF-e (Manifesto Eletrônico de Documentos Fiscais) no Deploy Agent traz para o Sankhya Om os manifestos rodoviários que o cliente já emitiu, junto com os eventos vinculados a eles.

Cada manifesto vira uma viagem com motoristas, veículo e documentos transportados. A importação não emite nem transmite MDF-e à SEFAZ.

## Antes de enviar

Peça ao cliente e confira:

- XMLs de MDF-e de emissão própria, do ambiente de produção e do modal rodoviário;
- XMLs de CT-e (Conhecimento de Transporte Eletrônico) e de NF-e referenciados pelos manifestos;
- XMLs de evento: cancelamento, encerramento, inclusão de condutor, inclusão de DF-e (Documento Fiscal Eletrônico) e pagamento da operação de transporte.

Você pode enviar tudo no mesmo lote: o Deploy Agent define a ordem de processamento.

Não são importados MDF-e de terceiros, do ambiente de homologação, dos modais aéreo, aquaviário e ferroviário, nem MDF-e cancelado na SEFAZ. O MDF-e também não é importado quando o CT-e referenciado não está no Sankhya Om (exceto em carga própria): envie o CT-e e reprocesse o MDF-e.

## Eventos

Sem os XMLs de evento, manifestos cancelados ou encerrados na SEFAZ ficam em aberto no Sankhya Om.

- **Quando são aplicados:** no fim da busca de arquivos, e só depois que não houver arquivo EFD pendente. O **Reprocessar Registro** não aplica eventos: se o MDF-e tiver eventos, faça uma nova busca de arquivos em seguida.
- **Eventos que não são aplicados:** evento não homologado pela SEFAZ, evento de um MDF-e que não está no Sankhya Om e qualquer evento de um MDF-e cancelado.
- **Cancelamento:** a SEFAZ não aceita cancelar um MDF-e já encerrado, então esse evento é desconsiderado.
- **Inclusão de DF-e:** vale apenas para MDF-e emitido com carregamento posterior. Cada NF-e do evento é vinculada se já estiver no Sankhya Om; as que faltarem ficam de fora até serem enviadas.
- **Reenvio:** eventos já aplicados são ignorados. A exceção é o evento de pagamento sem protocolo da SEFAZ, que é gravado de novo a cada envio e duplica os pagamentos.

## Cadastros gerados

### Motoristas e veículos

| Tipo de base | Motorista | Veículo |
| --- | --- | --- |
| Prospecção | Só com os dados do XML: nome e CPF. | Só com os dados do XML, incluindo a placa. |
| Cliente | Dados do XML, completados pela consulta do CPF em serviços externos. | Dados do XML, completados pela consulta da placa em serviços externos. Se a consulta falhar, fica só com os dados do XML. |

- **Cidade:** em base de prospecção, é a da empresa cadastrada no Sankhya Om; na falta dela, o município do emitente no XML e, por último, a cidade padrão. Em base cliente, a cidade do veículo vem da consulta ou, na falta dela, da cidade padrão.
- **Base de prospecção:** nenhum serviço externo é consultado. Cadastros com menos dados do que numa base cliente são o comportamento esperado.
- **Sem duplicidade:** motoristas e veículos que já existem são reaproveitados, o motorista pelo CPF e o veículo pela placa.
- **Dados ausentes:** sem CPF válido no XML, o motorista não é cadastrado; sem placa, o veículo não é cadastrado.

### Contratante e responsável pelo seguro

**Contratante:** quando o XML não informa o contratante e o veículo de tração não tem proprietário (frota própria), o emitente é usado como contratante. Se o contratante não for informado e o veículo tiver proprietário, o MDF-e não é importado.

**Responsável pelo seguro:** o Deploy Agent usa, nesta ordem:

1. o CPF ou CNPJ do emitente, quando ele é o responsável;
2. o CNPJ do responsável informado no MDF-e;
3. o CNPJ do contratante informado no grupo da ANTT do modal rodoviário.

Com o CNPJ em mãos, o Deploy Agent consulta os dados em serviços externos e cadastra o parceiro, se ele ainda não existir. Em base de prospecção, essa consulta não é feita. Se o XML não identificar o responsável, o MDF-e é importado sem ele.

### Empresa emitente

- **RNTRC:** se a empresa já tem outro RNTRC no cadastro, o cadastro é mantido. RNTRC que não tem 8 dígitos numéricos não é gravado.
- **Ambiente MDF-e:** o campo fica como **Produção**. Se a empresa precisar emitir MDF-e em homologação antes de entrar em produção, altere o campo manualmente no cadastro da empresa.

## Mensagens do log

As tabelas abaixo trazem as mensagens que pedem alguma ação. Os trechos entre colchetes, como [chave], são substituídos pelos dados do arquivo. Para consultar o log de um arquivo, confira o artigo [Enviar e reprocessar documentos fiscais](https://ajuda.sankhya.com.br/hc/pt-br/articles/44309970843159).

### Manifesto e cadastros

| Mensagem no log | O que fazer |
| --- | --- |
| "CT-e não encontrado na base. Chave do CT-e: [chave]" | Envie o CT-e e reprocesse o MDF-e. |
| "Nenhum documento encontrado para este MDFe." | O MDF-e não é de carga própria e não referencia CT-e. Confira o XML com o cliente. |
| "Documento não é de emissão própria." | Confira o CNPJ do emitente com o cliente. |
| "CPF do motorista ausente no XML" | Confira o XML com o cliente. Se precisar do motorista, cadastre-o como parceiro motorista. |
| "Placa do veículo ausente no XML" | Confira o XML com o cliente. Se precisar do veículo, cadastre-o. |
| "CNPJ do responsável ausente em infResp e infContratante" | Se precisar do responsável, cadastre-o como parceiro. |

### Empresa emitente

| Mensagem no log | O que fazer |
| --- | --- |
| "RNTRC do MDF-e [número/série] ([valor XML]) diverge do cadastro da empresa ([valor cadastro]). Cadastro mantido." | Confirme com o cliente qual é o correto e, se for o do XML, atualize o cadastro da empresa. |
| "RNTRC inválido no MDF-e [número/série]: [valor]. Cadastro da empresa não atualizado." | Confirme o RNTRC com o cliente e preencha no cadastro da empresa. |

### Eventos

| Mensagem no log | O que fazer |
| --- | --- |
| "Evento de [tipo] sem MDF-e correspondente: [chave]" | Peça o XML do MDF-e ao cliente, envie-o e faça uma nova busca de arquivos. |
| "Evento de [tipo] não homologado pela SEFAZ: [chave] [código - motivo do retorno]" | Confira com o cliente se existe uma versão homologada do evento e envie esse arquivo. |
| "Município de encerramento [código] não encontrado no ERP para o MDF-e [chave]" | Cadastre o município e preencha manualmente o município de encerramento do MDF-e. |
| "CPF do condutor inválido no evento do MDF-e [chave]: [CPF]" | O condutor não foi vinculado. Confira o arquivo com o cliente. |
| "NF-e [chave] do evento de inclusão de DF-e não encontrada no ERP. Importe a NF-e e reprocesse o evento" | Envie a NF-e e faça uma nova busca de arquivos. |
| "Chave de NF-e inválida no evento de inclusão de DF-e do MDF-e [chave MDF-e]: [chave NF-e]" | Só essa NF-e ficou de fora. Confira o arquivo com o cliente. |
| "CPF/CNPJ do responsável pelo pagamento inválido no evento do MDF-e [chave]: [documento]" | Nenhum pagamento foi registrado. Confira o arquivo com o cliente. |
| "Não foi possível registrar o pagamento da operação de transporte do MDF-e [chave]" | Faça uma nova busca de arquivos. Se a mensagem se repetir, acione o suporte da Sankhya. |

---

#### Saiba mais

- [Conheça o Deploy Agent](https://ajuda.sankhya.com.br/hc/pt-br/articles/43952524117911): visão geral, abas, indicadores e arquivos processados.
- [Enviar e reprocessar documentos fiscais](https://ajuda.sankhya.com.br/hc/pt-br/articles/44309970843159): envio de arquivos, reprocessamento e tratamento de erros.
- [Limites e dúvidas frequentes](https://ajuda.sankhya.com.br/hc/pt-br/articles/44309955184663): pontos de atenção e perguntas frequentes sobre o Deploy Agent.
