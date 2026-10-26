---
id: "44010698245271"
titulo: "[TMS] - Importação de arquivo EDI via Portal do Transportador"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010698245271--TMS-Importa%C3%A7%C3%A3o-de-arquivo-EDI-via-Portal-do-Transportador"
trilha: "Lincros > TMS > Operacional - TMS"
atualizado_em: "2026-10-05T18:43:45Z"
rotulos: ["sync_hc", "lincros", "lincros_13433313", "sync_hash_f50218587029"]
---

# [TMS] - Importação de arquivo EDI via Portal do Transportador

**Menu**: Operacional > Importação > EDI > Importação

**Objetivo**: A utilização de EDIs proporcionam ganho de agilidade, qualidade, custo e segurança na comunicação e nos processos em empresas, pois a troca eletrônica de dados (EDI) elimina a entrada manual (digitação). Com o emprego desta tecnologia as informações que saem de um sistema já darão entrada em outro, não dependendo de intervenção humana.

**Considerações**:

- Possuir arquivos EDI para importação;
- Tipos de EDI:

- NOTFIS - Quando o sistema do embarcador envia a transportadora um arquivo contendo os dados das notas fiscais das mercadorias a serem transportadas;
- CONEMB - Quando a transportadora envia ao embarcador um arquivo contendo a relação dos 'conhecimentos embarcados';
- DOCCOB - O envio de um arquivo contendo os conhecimentos faturados (fatura de transporte) da transportadora para o embarcador.
- OCOREN - Quando o sistema de uma transportadora (TMS) envia de volta ao embarcador um arquivo contendo as informações atualizadas referentes as coletas e entregas realizadas (ocorrências de transporte). Permite envio de anexos para serem anexados;
- PREFAT - O envio de um arquivo do embarcador à transportadora, contendo a 'pré-fatura de transporte', ou seja, os valores e conhecimentos que já foram liberados para faturamento;

A partir da necessidade de modernização e padronização dos arquivos EDIs para o ramo de transporte, a empresa Proceda criou modelos de arquivos EDIs que se adaptassem às necessidades das transportadoras. Os EDIs padrão Proceda se dividem em 5 tipos de arquivo: NOTFIS, CONEMB, DOCCOB, OCOREN E PREFAT.

Abaixo segue os procedimentos necessários:

**Seleção de embarcador:** Quando selecionado o embarcador na tela de importação, ao importar o arquivo, será utilizado o layout de EDI padrão no cadastro da transportadora empresa;

![Imagem 1: Seleção de embarcador: Quando selecionado o embarcador na tela de importação, ao importar o arquivo, será utilizado o…](https://lincros-20.intercom-attachments-7.com/i/o/xa2fv75n/1963369354/91caacdbbdbdcc04302552407a55/143D16425B83DB3B86CFE14000C8238B?expires=1791331200&signature=ffe2dd61bff825211e12dca5c38f378f21aa2e9fce5e054ea1d61fa3dd6e3e8e&req=dSkhFcp4lIJaXfMW3nq%2BgfWKjbaMuFwMkf5%2Bv9Kvy5gog1J9grUHDmYfWY9A%0AEOk2njf2Z4Phabm%2BUCOZumf%2BPuc%3D%0A)

**Entradas** - Arquivo txt seguindo o padrão EDI. Para saber quais padrões o sistema aceita e para realizar o download dos mesmos, acessar o artigo [[TMS] - Layouts dos arquivos padrões Proceda](https://sankhya.zendesk.com/hc/pt-br/articles/44010542169239);

- CONEMB
- DOCCOB
- NOTFIS
- OCOREN

Esse arquivo podem ser importado pela tela de Operacional > Importação > Arquivo EDI, pela rotina de importação através de email, FTP, um diretório específico, webservice.

Os detalhes da importação, como conteúdo e erros ocorridos podem ser verificados pela tela Operacional > Importação > Edição de importação EDI. A importação de EDI pode gerar diversas saídas, por exemplo:

- COB\_CORR gera uma fatura vinda dos Correios;
- OCORR gera uma ocorrência;
- OCORR\_XML gera um eventos de ocorrência;
- OCORTEXLOG, OCORTOTEXP e OCORTFO geram eventos de ocorrência;
- CONEMB gera um conhecimento de frete;
- DOCCOB gera uma fatura;
- DOCCOB\_CTS;
- RASTREIONF realiza a importação do código de rastreio;
- TRIANGULNF

**Saídas** - Arquivos de NOTFIS e PREFAT.

**Fluxo**: UML

![Imagem 2: Fluxo : UML](https://lincros-20.intercom-attachments-7.com/i/o/xa2fv75n/1963369380/789b58a34fb4d976ad4c3718137b/045A52DFC4A58EA4EE5F2D31C0C1C345?expires=1791331200&signature=d506815c252cc37ddc6d61db4d43518ea2fdc060bb702e8a9b2abfd229c1c563&req=dSkhFcp4lIJXWfMW3nq%2BgW0128s0i8Cgg8PuKDOTL3Q1uXnRqHIIdCZFYAhx%0ALfs4RsbxKhiZcCbI66Z5daQYR0M%3D%0A)

- COB\_CORR - ImportadorFaturaCorreios;
- OCORR - ImportadorOCORREN;
- OCORR\_XML - ImportadorOCORRENXML;
- OCORTEXLOG - ImportadorTexlogOCORREN;
- OCORTOTEXP - ImportadorTotalExpressOCORREN;
- OCORTFO - ImportadorTransfolhaOCORREN;
- CONEMB - ImportadorCONEMB;
- DOCCOB - ImportadorDOCCOB;
- DOCCOB\_CTS - ImportadorDOCCOBCTS;
- RASTREIONF - ImportadorRASTREIONF;
- TRIANGULNF - ImportadorTRIANGULACAONF

**Anexos de OCORR** - É possível enviar anexos aos eventos de ocorrência através da importação de arquivos via e-mail ou FTP. Para mais informações de como funciona o processo, consultar a documentação [[TMS] - Anexos do OCOREN (ocorrências)](https://sankhya.zendesk.com/hc/pt-br/articles/44010698245271).

**Obs:** O Sistema não irá importar o anexo se ele estiver zipado.

"Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos"
