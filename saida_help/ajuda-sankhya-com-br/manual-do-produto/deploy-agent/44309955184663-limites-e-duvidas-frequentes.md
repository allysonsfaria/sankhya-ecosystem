---
id: "44309955184663"
titulo: "Limites e dúvidas frequentes"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44309955184663-Limites-e-d%C3%BAvidas-frequentes"
trilha: "Manual do Produto > Inteligência e Análise > Deploy Agent"
atualizado_em: "2026-10-21T20:07:09Z"
---

# Limites e dúvidas frequentes

Este artigo reúne os limites de funcionamento do Deploy Agent e as dúvidas mais comuns sobre o processamento. Para conhecer o módulo, confira o artigo [Conheça o Deploy Agent](https://ajuda.sankhya.com.br/hc/pt-br/articles/43952524117911).

## Pontos de atenção

- **Limpeza antes de reprocessar em volume.** Reprocessar um artefato ou documento fiscal sem limpar dados anteriores pode gerar registros duplicados, perder referências de dados já modificados ou deixar dados inconsistentes. Antes de reprocessar um grande volume, faça backup do banco ou trabalhe num ambiente de staging.
- **Processamento sequencial e paralelo.** NF-e, NFC-e, CT-e e EFD são processadas sequencialmente por tipo de documento; e-Social segue a ordem de data do evento. NFS-e usa fila de processamento e pode ser processada em paralelo. Enviar vários arquivos do mesmo tipo para o mesmo período não trava o sistema: eles são enfileirados e processados um a um.
- **Arquivos temporários.** Os arquivos baixados do repositório ficam numa pasta temporária do servidor para acesso rápido. A cada novo processamento, a pasta atual é rotacionada (renomeada) e sua exclusão ocorre em segundo plano, sem bloquear o início do novo processamento; uma pasta nova é criada para os arquivos recebidos. Por isso, um arquivo processado recentemente pode ser consultado direto da pasta temporária, sem refazer a busca no repositório. Pastas antigas são limpas automaticamente após um prazo definido pelo ambiente.
- **Divisão automática de EFD grande.** Arquivos EFD acima de 50 MB são divididos automaticamente em partes de até 10.000 registros por tipo de documento, sem necessidade de divisão manual. Cada parte vira um evento próprio e é processada em sequência, mas os dados descobertos numa parte (produtos, parceiros, impostos) ficam disponíveis para as partes seguintes. Se uma parte falhar, reprocesse apenas ela; as demais permanecem processadas.
- **Impacto fiscal de operações processadas.** Ao importar NF-e, EFD ou NFS-e, os impostos são calculados e registrados, as operações aparecem na posição fiscal e os valores são consolidados na contabilidade. Se um arquivo estava incorreto, a correção não é automática: identifique o erro pelo log, cancele manualmente a operação no ERP e reimporte o arquivo corrigido.
- **Sincronização com a API remota.** O Deploy Agent notifica a API de Melhores Práticas ao final de cada processamento. Se a notificação falhar, o processamento local é concluído normalmente (os dados já foram inseridos no banco) e você recebe um aviso; na próxima consulta, o status é replicado para a API.
- **Ambiente em uso por outra pessoa.** Como a implantação altera dados compartilhados, o Deploy Agent controla quem está usando o ambiente. Quando outra pessoa já está processando, ações como **Reprocessar** e **Cancelar** ficam bloqueadas, com a indicação "Ambiente em uso por: [nome]". Quando você mesmo já ocupava o ambiente e inicia uma nova ação, o sistema confirma antes: "Sobrescrever o próprio ambiente — Você está sobrescrevendo o ambiente que você mesmo ocupou. Deseja continuar?"

## Perguntas frequentes

**Como limpo os dados do banco para refazer um setup?**

Use a limpeza de base, disponível em ambientes de prospecção. O passo a passo está no artigo [Enviar e reprocessar documentos fiscais](https://ajuda.sankhya.com.br/hc/pt-br/articles/44309970843159), em **Limpar a base de prospecção**. A limpeza remove as tabelas de configuração (artefatos importados, eventos processados) e preserva a estrutura base do Sankhya Om. Execute apenas em staging; em produção, faça backup antes de qualquer limpeza.

**Por que o sistema me bloqueia de instalar um artefato?**

As causas mais comuns são: um pré-requisito ainda não instalado (por exemplo, Composição de Produto exige Produtos já instalado), dados inconsistentes no arquivo (CNPJ duplicado, CPF inválido), um parâmetro obrigatório não preenchido, ou um recurso desativado no ambiente (como o WMS). Consulte o log de erro para identificar a causa exata.

**Quanto tempo leva para processar um arquivo grande?**

Depende do tamanho, da complexidade (documentos com muitos impostos levam mais tempo) e da carga do servidor e do banco no momento. Um EFD de 100 MB pode levar de 10 a 30 minutos. Processe arquivos grandes fora de horários de pico.

**Posso cancelar um processamento em andamento?**

Sim. O passo a passo está no artigo [Enviar e reprocessar documentos fiscais](https://ajuda.sankhya.com.br/hc/pt-br/articles/44309970843159), em **Cancelar o processamento**. Os cadastros já realizados até o momento do cancelamento permanecem no sistema; você pode retomar depois pelo reprocessamento.

**Como sei se um documento fiscal foi processado corretamente?**

Verifique o status na aba **Arquivos processados** (confira [Conheça o Deploy Agent](https://ajuda.sankhya.com.br/hc/pt-br/articles/43952524117911)), confira se a nota aparece com os dados completos na tela de origem no ERP e compare os valores com o relatório de apuração de ICMS/PIS, quando aplicável.

**O Deploy Agent suporta múltiplas empresas no mesmo processamento?**

Sim. O sistema identifica cada empresa pelo CNPJ presente no arquivo, cria o cadastro quando ainda não existe e associa as operações à empresa correta. Ao final, um relatório consolidado mostra quantas operações foram processadas por empresa.

**Como peço suporte quando algo dá errado?**

Verifique o log do servidor de aplicação e o log de eventos do processo, e ative o nível de log de depuração antes de reprocessar, se precisar de mais detalhe. Ao contatar o suporte da Sankhya, reúna o arquivo original (quando a privacidade permitir), os logs completos, capturas de tela da tela onde ocorreu o problema e a versão do módulo em uso. Confira [Canais de atendimento e abertura de chamados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360059840413-Canais-de-atendimento-e-abertura-de-chamados).
