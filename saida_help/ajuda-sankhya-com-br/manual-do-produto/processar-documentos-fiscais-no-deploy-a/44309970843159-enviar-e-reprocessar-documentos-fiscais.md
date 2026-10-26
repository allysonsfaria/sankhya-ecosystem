---
id: "44309970843159"
titulo: "Enviar e reprocessar documentos fiscais"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44309970843159-Enviar-e-reprocessar-documentos-fiscais"
trilha: "Manual do Produto > Inteligência e Análise > Deploy Agent > Processar documentos fiscais no Deploy Agent"
atualizado_em: "2026-10-21T21:03:49Z"
---

# Enviar e reprocessar documentos fiscais

O [Deploy Agent](https://ajuda.sankhya.com.br/hc/pt-br/articles/43952524117911) processa documentos fiscais já emitidos pelo cliente para pré-popular o banco com as operações, parceiros, produtos e movimentações registrados neles, reduzindo o quanto você pessoa implantadora precisa lançar manualmente. É um processamento em lote de arquivos históricos, não uma captura em tempo real.

## Antes de começar

Confirme que os arquivos estão em formato válido:

| Documento | Formato esperado |
| --- | --- |
| NF-e, NFC-e, CT-e e NFS-e | XML assinado |
| EFD | Texto estruturado |
| e-Social | XML ou estruturado conforme o padrão da Receita |

## Enviar arquivos para processamento

O envio é o mesmo para qualquer tipo de documento. O que muda é por onde os arquivos chegam:

| Quem envia | Onde |
| --- | --- |
| O prospect | No Portal Deploy |
| A equipe de serviços | No Deploy Agent |

### Arquivos enviados pelo prospect, no Portal Deploy

> **ℹ️ Nota**
>
> A opção só aparece em ambientes com integração ativa com o Portal Deploy.

1. Acesse o **Deploy Agent** e clique em **Consulta do Portal Deploy**, na barra superior.
2. Selecione a oportunidade do prospect. A lista mostra empresa, CNPJ e total de arquivos, e pode ser filtrada por data de início e período dos documentos.
3. Clique em **Iniciar processamento** e acompanhe o andamento na tela do Deploy Agent.

Quando não houver oportunidades, a tela mostra que nenhuma está disponível. Se a lista não carregar, tente consultar novamente.

### Arquivos enviados pela equipe de serviços, no Deploy Agent

1. Insira os arquivos no repositório.
2. Acesse o **Deploy Agent** e clique em **Reprocessar**, na barra superior.
3. Marque os modelos de documento que você enviou e marque **Buscar novos arquivos no repositório**.
4. Clique em **Confirmar** e acompanhe o indicador de status até ficar **Concluído**.

## Reprocessar documentos

Use este fluxo quando quiser reiniciar o processamento escolhendo quais tipos de documento reprocessar.

> **ℹ️ Nota**
>
> O reprocessamento fica indisponível enquanto há processamento em andamento.

1. Acesse o **Deploy Agent** e clique em **Reprocessar**, na barra superior.
2. Selecione os modelos de documento a reprocessar: CF-e, CT-e, e-Social, EFD, MDF-e, NF-e, NFC-e, NFCom e/ou NFS-e. Por padrão, todos vêm marcados.
3. Marque **Buscar novos arquivos no repositório**, se quiser incluir arquivos novos no reprocessamento.
4. Clique em **Confirmar** para iniciar, ou em **Cancelar**, na janela, para desistir sem reprocessar.
5. Acompanhe o andamento na tela do Deploy Agent.

Para reprocessar um único arquivo, use **Reprocessar Registro**, na aba **Arquivos processados**.

### Cancelar o processamento

> **ℹ️ Nota**
>
> O botão **Cancelar** só fica disponível com o processamento **Em andamento**.

1. Acesse o **Deploy Agent** e confirme que o status está **Em andamento**.
2. Clique em **Cancelar**, na barra superior.
3. Leia a confirmação: "Cancelar o processamento — Ao cancelar, o processamento dos arquivos será interrompido imediatamente. Os cadastros já realizados até o momento serão mantidos no sistema. Caso deseje reiniciar o processamento, utilize o botão Reprocessar. Deseja mesmo cancelar?"
4. Clique em **Sim** para confirmar, ou em **Não** para manter o processamento.

O cancelamento não desfaz os cadastros e movimentos já gerados antes da interrupção. Para retomar, use [Reprocessar documentos](https://ajuda.sankhya.com.br/hc/pt-br/articles/44309970843159-Enviar-e-reprocessar-documentos-fiscais#reprocessar-documentos).

## Tratar erros de processamento

Se um arquivo falhar, o erro é registrado no log e o processamento para apenas naquele arquivo; os demais seguem normalmente. Dados parcialmente inseridos não são revertidos automaticamente.

1. Acesse o **Deploy Agent** e abra a aba **Arquivos processados**.
2. Filtre pelo status **Erro** e, se quiser, pelo tipo de documento.
3. Selecione um único arquivo e clique em **Ver Documento** para conferir o conteúdo.
4. Identifique a causa. Para MDF-e e NFS-e, confira o artigo específico do documento nesta seção.
5. Corrija a causa e acione **Reprocessar Registro**, ou exclua o registro com **Excluir Registro**, quando for o caso.

### Limpar a base

Use este fluxo para reiniciar um ambiente de prospecção ou demonstração.

> **Atenção:**
> Disponível apenas em ambientes de prospecção. A exclusão é permanente: confirme o escopo antes de prosseguir.

1. Acesse o **Deploy Agent** e clique em **Limpeza de Base**, na barra superior.
2. Escolha o escopo: **Apenas Sankhya** ou **Sankhya e BUs**.
3. Clique em **Confirmar**.
4. Leia a mensagem de confirmação, que informa que os dados serão excluídos permanentemente, e clique em **Sim** para confirmar ou em **Não** para desistir.
5. Aguarde a conclusão da limpeza e leia a mensagem final, que indica se a limpeza ocorreu apenas na Sankhya ou em todos os sistemas, conforme o escopo escolhido.

A limpeza **Apenas Sankhya** exclui os dados da base que estão no Sankhya Om. Já a opção **Sankhya e BUs** apaga os dados do Sankhya Om e do ambiente do Sankhya Tax.

## Documentos suportados

Os tipos de documento abaixo podem ser processados pelo Deploy Agent. MDF-e e NFS-e têm regras próprias, descritas em artigos específicos desta seção.

| Documento | O que extrai | Comportamento |
| --- | --- | --- |
| NF-e | Empresas, parceiros, produtos, operações de entrada e saída, impostos (ICMS, IPI, PIS, COFINS) e títulos financeiros | Cancelamentos são processados marcando a nota como cancelada |
| NFC-e | Operações de varejo direto ao consumidor, com imposto simplificado (ICMS) | Volume tipicamente maior de operações pequenas; integração com PDV |
| CT-e | Transportadores, parceiros de origem e destino, frete e impostos | O transportador é registrado como parceiro; o frete gera título financeiro |
| CF-e | Confira o cartão **CF-e** da aba **Resumo** | — |
| NFCom | Confira o cartão **NFCom** da aba **Resumo** | — |
| EFD | Aquisições, vendas, devoluções e apuração de ICMS e PIS/COFINS de um período | Arquivos acima de 50 MB são divididos automaticamente; confira o artigo [Limites e dúvidas frequentes](https://ajuda.sankhya.com.br/hc/pt-br/articles/44309955184663) |
| e-Social | Empresas, funcionários, admissões e desligamentos, folha e afastamentos | Gera impactos contábeis (débito em folha, crédito em contas a pagar); acompanhe na aba **Detalhamento E-Social** |
| MDF-e | Manifestos rodoviários e eventos vinculados | Confira o artigo [Regras de importação de MDF-e no Deploy Agent](https://ajuda.sankhya.com.br/hc/pt-br/articles/44309950201623) |
| NFS-e | Prestador, tomador, serviço e tributos municipais | Passa por conversão assistida por IA; confira o artigo [Regras de importação de NFS-e no Deploy Agent](https://ajuda.sankhya.com.br/hc/pt-br/articles/44309955264919) |

---

#### Saiba mais

- [Conheça o Deploy Agent](https://ajuda.sankhya.com.br/hc/pt-br/articles/43952524117911): visão geral, abas, indicadores e arquivos processados.
- [Regras de importação de MDF-e no Deploy Agent](https://ajuda.sankhya.com.br/hc/pt-br/articles/44309950201623) e [Regras de importação de NFS-e no Deploy Agent](https://ajuda.sankhya.com.br/hc/pt-br/articles/44309955264919): regras e tratamento de erros por tipo de documento.
- [Limites e dúvidas frequentes](https://ajuda.sankhya.com.br/hc/pt-br/articles/44309955184663): pontos de atenção e perguntas frequentes sobre o Deploy Agent.
