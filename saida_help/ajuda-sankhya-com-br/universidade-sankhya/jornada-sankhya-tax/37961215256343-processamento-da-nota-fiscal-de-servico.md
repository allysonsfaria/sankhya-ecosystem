---
id: "37961215256343"
titulo: "Processamento da Nota Fiscal de Serviço"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37961215256343-Processamento-da-Nota-Fiscal-de-Servi%C3%A7o"
trilha: "Universidade Sankhya > Jornada Sankhya Tax"
atualizado_em: "2026-09-30T13:29:52Z"
rotulos: ["Configuração", "Parceiro", "Importação", "Prefeituras", "NFS-e", "Documentos Eletrônicos"]
---

# Processamento da Nota Fiscal de Serviço

## Captura e Importação de Nfse

#### O que é esta ferramenta e qual a importância dessa funcionalidade para a gestão da empresa?

O Processamento da NFSe é o recurso do Sankhya TAX que organiza, valida e integra as notas fiscais de serviço recebidas pela empresa. As notas chegam ao sistema por meio da integração com o ASIS, que captura os documentos diretamente no ambiente das prefeituras dos municípios. Quando os dados estão completos, a nota é processada automaticamente; se houver divergências ou informações faltantes, ela aparece na tela de processamento para vinculação manual.

Sua importância está em garantir que apenas documentos válidos e consistentes avancem para as rotinas de compras, financeiras e contábeis. Isso assegura a integridade das informações, evita erros e dá rastreabilidade total às operações de serviço.

#### Quais problemas este recurso resolve?

- Entrada manual repetitiva de dados de notas fiscais de serviço.
- Falta de controle sobre divergências e inconsistências.
- Risco de notas em duplicidade nos registros.
- Pagamentos indevidos ou incorretos.
- Relatórios contábeis distorcidos por dados não validados.

#### Quais os riscos de não auditar as notas fiscais de serviço tomadas?

Sem o Captura e Importação de Nfse, a empresa fica exposta a inconsistências fiscais e financeiras, falta de rastreabilidade e maior risco de retrabalho. Notas incorretas podem ser integradas sem validação, gerando impactos na contabilidade, distorções nos relatórios gerenciais e até pagamentos duplicados. Além disso, a ausência desse controle reduz a segurança das operações e pode comprometer a confiabilidade da gestão empresarial.

#### Cenário de aplicação

A Axis LTDA., empresa de serviços de TI, recebe mensalmente diversas NFSes de fornecedores em diferentes municípios. Até pouco tempo atrás, os analistas precisavam baixar manualmente as notas no portal de cada prefeitura e lançar os dados no ERP, o que gerava risco de duplicidade, inconsistências e até pagamentos incorretos.

Com o recurso de Captura e Importação de NFSe, o Sankhya TAX passou a integrar automaticamente as notas emitidas contra a Axis diretamente do ambiente das prefeituras. Notas completas são processadas sem intervenção; já as que apresentam divergências, como ausência de natureza de operação ou fornecedor não cadastrado, ficam sinalizadas para tratativa. Assim, a equipe consegue corrigir rapidamente as informações e garantir que apenas documentos válidos avancem para as rotinas de compras, financeira e contábil.

**Tarefa:** Assista ao vídeo de demonstração prática e, em sua base de testes, acesse a rotina de Captura e Importação de NFSe. Localize uma nota com divergência, valide os dados obrigatórios (como operação, negociação e fornecedor) e processe a nota até que esteja pronta para integração com a Central de Compras.

#### Demonstração prática no sistema

[Vídeo: tutorial do artigo](https://player.vimeo.com/video/1127582359)

#### É o momento de aplicar o conhecimento adquirido! Execute as movimentações no ERP Sankhya

**Atenção!** **O funcionamento deste recurso está condicionado ao procedimento detalhado no manual Script de integração.**

1. Acesse a tela **Captura e Importação de Nfse**
   **Menu:** Configurações » Rotinas » Captura e Importação de Nfse

- Após a integração as notas capturadas aparecerão na grade de resultados apresentando como primeira informação seu Status de Integração.
- Selecione com um duplo clique a nota “**Com** **divergência**”.
- Na lateral esquerda, a seção **Divergências encontradas** apresenta todas as inconsistências encontradas na captura, as inconsistências podem ser tratadas manualmente ou de forma automática ao vincular um modelo padrão.

2. **Para tratativa manual**

**Aba Informações da Nota**

- Alimente os campos abaixo com seus respectivos dados:

  - **Empresa**
  - **Tipo Operação**
  - **Tipo Negociação**
  - **Natureza** (opcional)
    O parâmetro **EXIGNATCFR - Exigir natureza na central/financeiro/rateio?** irá definir se o preenchimento da Natureza será obrigatório.
  - **Projeto** (opcional)
  - **Centro Resultado** (opcional) 
    O parâmetro **EXIGCRCFR - Exigir CR na central/financeiro/rateio?** irá definir se o preenchimento do Centro Resultado será obrigatório.

**Atenção!**
Os parâmetros mencionados afetam diretamente os resultados gerencias e devem ser manipulados com cautela, seguindo as diretrizes de gestão da empresa.

**TPVSEMVALNATCUS - Lista Tip.Mov. sem validação EXIGNATCFR/EXIGCRCFR**
Esse parâmetro define uma lista de Tipos de Movimento que ficarão isentos da exigência dos parâmetros, logo, se o Tipo de Movimento da nota estiver incluída na lista deste parâmetro, os campos Natureza e Centro de Resultado continuam sendo exibidos, mas não serão obrigatórios, mesmo que o sistema esteja configurado para exigi-los, em geral.

**Aba Dados do Fornecedor**

- O campo Parceiro é alimentado caso o CNPJ da nota esteja vinculado a um fornecedor cadastrado na tela Parceiros.
- Se necessário, realize o cadastro seguindo orientações do manual “Configurações e cadastros básicos relacionados”

**Aba Serviço Prestado**

- Em divergencia de serviço não localizado devido duplicidade do tipo de serviço, localize no campo correspondente o serviço tomado.
- Caso não haja cadastro para a aquisição, utilize as orientações do manual “Configurações e cadastros básicos relacionados” para o cadastro de Tipo de Serviço e Serviço.
- Clique em “**Validar**” para processar a nota.

3. **Para tratativa via cadastro prévio**

**Aba Informações da Nota**

- Na seção de **Modelos de notas/pedidos** utilize os filtros para localizar o modelo correspondente.
- Marque o registro e em seguida acione o botão “**Aplicar** **modelo selecionado**” para vincular. 
  Caso seja necessário, o manual “Configurações e cadastros básicos relacionados” contém orientações sobre cadastro de novos modelos de notas/pedidos

**Aba Dados do fornecedor**

- Na seção **Fornecedores** utilize os filtros para localizar o fornecedor desejado.
- Marque o registro na grade e acione o botão “**Aplicar** **fornecedor selecionado**”.

**Aba Serviço Prestado**

- Na seção **Serviços** utilize os filtros para localizar o serviço correspondente.
- Marque o registro na grade e acione o botão “**Aplicar** **serviço selecionado**”.
- Clique em “**Validar**” para processar a nota.

4. **Para abrir a nota na Central de Compras**

- Na grade de resultados da tela Captura e Importação de Nfse, localize a coluna **Nota Integrada**.
- Clique sobre o número para ser direcionado à Central de Compras. 
  As notas capturadas são sinalizadas no campo Observação com a informação “| Nota importada via API |” destacada.
