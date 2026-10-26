---
id: "37033361858583"
titulo: "1021 Rejeição: Grupo IBS/CBS informado indevidamente"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37033361858583-1021-Rejei%C3%A7%C3%A3o-Grupo-IBS-CBS-informado-indevidamente"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-07-22T14:22:00Z"
rotulos: ["NF-e", "XML", "SEFAZ", "Impostos", "1021 Rejeição", "Grupo IBS/CBS informado indevidamente", "ind_gIBSCBS", "Rejeição 1021", "Reforma Tributária"]
---

# 1021 Rejeição: Grupo IBS/CBS informado indevidamente

**MENSAGEM**

1021 Rejeição: Grupo IBS/CBS informado indevidamente [nItem: 999]

**SITUAÇÃO**

Ao tentar emitir uma Nota Fiscal Eletrônica (NF-e) ou Nota Fiscal de Consumidor Eletrônica (NFC-e), o sistema apresenta a rejeição informando que o **grupo IBS/CBS** foi informado indevidamente para um determinado item da nota fiscal. Esta rejeição ocorre quando o CST do IBS/CBS utilizado no documento fiscal possui um indicador que **não permite** a informação do grupo IBS/CBS (ind\_gIBSCBS = 0), mas mesmo assim o grupo foi informado no XML.

**SOLUÇÃO**

(1)** Verifique a versão do sistema Sankhya Om instalada.**

As versões que contemplam a correção são:

- 4.34b225
- 4.35b221
- Livros Fiscais: 5.16.6

Caso o ambiente esteja em versão inferior, solicite a atualização para a versão mais recente disponível.

**OBSERVAÇÃO:** Mesmo após a atualização, caso a rejeição persista, siga o passo a passo abaixo:

**(1)** Verifique o CST do IBS/CBS utilizado no documento fiscal:

- Acesse o **"Portal de Vendas"** (Comercial » Consulta » Portal de Vendas)
- Localize a nota fiscal rejeitada
- Clique em **"Gerar XML"** para visualizar o arquivo XML da nota
- Identifique o item que está gerando a rejeição (indicado pelo número no campo [nItem: 999])
- Verifique o CST do IBS/CBS informado na tag **IBSCBS/CST**
- Observe se o grupo **gIBSCBS** está sendo informado indevidamente para este CST

**(2)** Consulte a tabela oficial de CSTs válidos para o IBS/CBS:

- Acesse o **"Portal Nacional da NF-e"** (https://www.nfe.fazenda.gov.br)
- Navegue até a aba **"Documentos"**, opção **"Diversos"**
- Localize a **"Tabela de Código de Situação Tributária (CST) do IBS e da CBS"**
- Verifique o indicador **ind\_gIBSCBS** para o CST utilizado
- Confirme se o CST utilizado possui indicador **ind\_gIBSCBS = 0**, o que significa que **não permite** a informação do grupo IBS/CBS

**(3)** Verifique as alíquotas de IBS/CBS:

- Acesse **"Alíquotas de IBS/CBS"** (Fiscal » Cadastros » Alíquotas » Alíquotas de IBS/CBS)
- Localize a alíquota utilizada para o produto em questão
- Verifique o campo **"CST"** configurado
- Confirme se o CST configurado é compatível com a operação e se realmente não deve ter valores de IBS/CBS informados
- Se necessário, altere para um CST adequado à operação, observando a tabela oficial

**(4)** Verifique a configuração do produto:

- Acesse **"Produto"** (Configurações » Cadastros » Produtos » Produtos)
- Localize o produto que está gerando a rejeição
- Verifique se o produto está corretamente associado à alíquota de IBS/CBS
- Confirme se a configuração do produto está correta para o tipo de operação

**(5)** Refaça o processo de emissão da nota fiscal:

- Inutilize a numeração da nota rejeitada
- Exclua a nota com problema
- Refaça o processo de emissão da nota fiscal com as configurações corretas de CST do IBS/CBS
- Verifique se o XML gerado está de acordo com as regras de validação da SEFAZ

**CAUSA**

Esta rejeição ocorre devido à implementação da Reforma Tributária, conforme a Lei Complementar 214/2025. De acordo com a regra de validação da SEFAZ (UB13-20), quando o CST do IBS/CBS informado possui indicador que **não permite** a informação do IBS/CBS (ind\_gIBSCBS = 0), o sistema verifica se o grupo gIBSCBS foi informado indevidamente no XML.

A rejeição 1021 é gerada quando o sistema identifica que o CST informado na tag IBSCBS/CST possui indicador ind\_gIBSCBS = 0, mas mesmo assim o grupo gIBSCBS foi informado no XML. Isso pode ocorrer devido a:

- Configuração incorreta das alíquotas de IBS/CBS
- Utilização de CST incompatível com a operação realizada
- Falha na parametrização do sistema para a Reforma Tributária
- Inconsistência entre o CST informado e os valores de IBS/CBS preenchidos
- Erro na geração do XML pelo sistema, incluindo o grupo gIBSCBS quando não deveria

É importante ressaltar que cada CST do IBS/CBS possui indicadores específicos que determinam se o grupo gIBSCBS deve ou não ser informado no documento fiscal. Estes indicadores estão definidos na tabela oficial de CSTs do IBS/CBS, disponível no Portal Nacional da NF-e, e devem ser rigorosamente observados para evitar rejeições.
