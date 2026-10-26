---
id: "44010050392599"
titulo: "[TMS] - CT-e enviado pela transportadora não aparece no TMS e não há registro no log de importação"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010050392599--TMS-CT-e-enviado-pela-transportadora-n%C3%A3o-aparece-no-TMS-e-n%C3%A3o-h%C3%A1-registro-no-log-de-importa%C3%A7%C3%A3o"
trilha: "Lincros > TMS > Operacional - TMS"
atualizado_em: "2026-10-05T18:29:24Z"
rotulos: ["sync_hc", "lincros_17269556", "sync_hash_ef838e3db202", "lincros"]
---

# [TMS] - CT-e enviado pela transportadora não aparece no TMS e não há registro no log de importação

**Menu**:

1. Para consultar o CT-e > Documentos eletrônicos > CT-es
2. Para consultar o log de importação > Operacional > Importação > CT-e/NFS-e > Log
3. Para importar manualmente > Operacional > Importação > CT-e > Importação
4. Para conferir o cadastro da transportadora > Cadastro Geral > Transportadora > Transportadora Empresa > Cadastro

**Objetivo**: Orientar a investigação quando a transportadora informa que enviou o XML do CT-e (por e-mail ou FTP), mas o CT-e não aparece no TMS e não existe nenhum registro no log de importação.

**Considerações**:

- A transportadora envia os arquivos automaticamente (e-mail ou FTP) e as notas fiscais ficam sem CT-e vinculado;
- Ao pesquisar o CT-e (número ou chave) em Documentos eletrônicos > CT-es, nenhum registro é encontrado, e o log de importação não tem linha correspondente ao envio.

## Por que ocorre esta situação?

O log de importação só registra arquivos que chegaram até a rotina de importação do TMS. Se não há CT-e e não há linha no log, o mais provável é que o arquivo **não chegou ao TMS** e, nesse caso, não há mensagem de erro a ser consultada, porque a importação nem chegou a ser tentada.

## Importante — diferença entre os cenários

- **CT-e existe no TMS, mas sem chave e sem XML:** foi importado por outro caminho (por exemplo, EDI CONEMB). Veja o artigo "Importação Correta de CT-e no Sistema TMS: Como Garantir a Inclusão da Chave e XML";
- **CT-e existe no TMS com erro:** abra o CT-e e leia a seção 'Mensagem de importação', que indica o motivo da falha;
- **CT-e não existe e não há log:** siga este artigo.

## Causas mais comuns

**1. Endereço de destino incorreto.** O sistema de emissão da transportadora está configurado com um endereço ligeiramente diferente do endereço de recebimento da empresa (por exemplo, uma letra a menos no nome ou domínio incompleto, sem o ".com.br"). Mesmo um pequeno desvio faz com que os arquivos nunca cheguem ao TMS. O envio intermitente (alguns e-mails chegam e outros não) também pode indicar este problema em apenas alguns disparos.

**2. Recusa do e-mail antes de chegar ao TMS.** Se o servidor de envio da transportadora (ou do sistema de gestão que ela utiliza) estiver temporariamente em uma lista pública de bloqueio por reputação (blacklist), o servidor de recebimento pode recusar a mensagem. Nesse caso, o remetente recebe um retorno de erro (bounce, como um erro 550) e o TMS não recebe o arquivo nem gera log. A correção é feita do lado do remetente: solicitar a remoção do servidor da lista de bloqueio e, enquanto isso não ocorre, evitar o uso do servidor afetado.

**3. Padrão EDI não configurado no cadastro da transportadora** (somente para arquivos EDI enviados por e-mail). Sem esse padrão, os arquivos são ignorados sem apresentar erro. Veja o artigo "[Arquivos EDIS não estão sendo importados via E-mail, porém CT-Es da mesma transportadora sim](https://suporte.lincros.com/pt-BR/articles/13432974-tms-arquivos-edis-nao-estao-sendo-importados-via-e-mail-porem-ct-es-da-mesma-transportadora-sim)".

## Como investigar

1. Pesquise o CT-e pelo número ou chave em Documentos eletrônicos > CT-es. Se existir, consulte a 'Mensagem de importação';
2. Se não existir, consulte o log em Operacional > Importação > CT-e/NFS-e > Log, filtrando pela data do envio. Se não houver linha, o arquivo não chegou;
3. Confira com a transportadora o endereço exato de destino que está configurado no sistema de emissão dela, comparando caractere por caractere com o endereço de recebimento da sua empresa;
4. Solicite à transportadora o log de envio do sistema de emissão dela (data, hora e destino dos disparos) e, se possível, o e-mail original exportado em formato .eml (não encaminhado), que preserva os cabeçalhos técnicos;
5. Confirme com a transportadora se houve retorno de erro (bounce) nos disparos que falharam;
6. Para regularizar os documentos pendentes, solicite o reenvio dos XMLs (muitos sistemas de emissão permitem o reenvio retroativo por período) ou importe os XMLs manualmente em Operacional > Importação > CT-e > Importação;
7. Se a transportadora não conseguir usar o e-mail, avalie o envio por FTP. Veja o artigo "Envio de CT-e e EDI pela transportadora via pasta FTP".

**Observação**: nem toda nota fiscal sem CT-e indica falha de envio. Notas canceladas ou operações em que o CT-e ainda não foi emitido também aparecem sem CT-e vinculado. Valide esses casos antes de abrir o chamado.

**Como solicitar suporte**: Se o endereço de destino estiver correto e a transportadora comprovar o envio, abra um chamado informando:

- Chave de acesso e número do CT-e de exemplo, com data e hora do envio;
- Endereço de destino utilizado pela transportadora;
- Log de envio da transportadora e, se disponível, o e-mail original (.eml);
- Lista das notas fiscais afetadas e o período do problema.

"Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos".
