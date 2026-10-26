---
id: "44010049903511"
titulo: "[TMS] - Envio de CT-e e EDI pela transportadora via pasta FTP"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/44010049903511--TMS-Envio-de-CT-e-e-EDI-pela-transportadora-via-pasta-FTP"
trilha: "Lincros > TMS > Operacional - TMS"
atualizado_em: "2026-10-05T18:29:19Z"
rotulos: ["sync_hc", "lincros_17269585", "lincros", "sync_hash_7a914cb7c9fe"]
---

# [TMS] - Envio de CT-e e EDI pela transportadora via pasta FTP

**Menu**:

Importar manualmente = Operacional > Importação > CT-e > Importação
Consultar o log de importação = Operacional > Importação > CT-e/NFS-e > Log

**Objetivo**: Explicar como a transportadora pode enviar os arquivos de CT-e e EDI para o TMS por pasta FTP, como alternativa ao envio por e-mail.

**Considerações**:

- A transportadora não consegue cadastrar ou utilizar o endereço de e-mail de recebimento da empresa, ou o envio por e-mail está instável;
- A solicitação de criação do acesso é feita ao suporte Lincros.

## Como funciona

Neste modelo, é a transportadora quem envia os arquivos para uma pasta FTP da Lincros. O TMS lê a pasta automaticamente e importa os arquivos, sem necessidade de digitação ou de importação manual.

## Passo a passo

1. Abra um chamado com o suporte Lincros solicitando o envio por FTP para a transportadora, informando o **CNPJ da transportadora** e o **e-mail de um contato da própria transportadora** (é esse e-mail que será utilizado para o cadastro da senha de acesso);
2. O suporte Lincros cria um usuário de **WebService** para a transportadora (caso ainda não exista) e informa o endereço do servidor, a porta e o diretório da empresa;
3. Encaminhe estas informações à transportadora. Elas serão utilizadas para acessar a pasta por meio de um programa de transferência de arquivos (por exemplo, o WinSCP);
4. Após fazer login, a transportadora deve enviar os arquivos para o diretório informado. Eles serão importados automaticamente para o TMS;
5. Defina com a transportadora a versão e o layout dos arquivos que serão enviados (por exemplo, o layout e a versão do CONEMB). Se o layout configurado na Lincros não for o mesmo que a transportadora utiliza, informe no chamado para que o ajuste seja feito;
6. Após os primeiros envios, confira o resultado em Operacional > Importação > CT-e/NFS-e > Log.

## Atenção

- O campo de FTP existente no cadastro da Transportadora (Empresa) pertence a outro fluxo de acesso ao FTP e não deve ser usado para esta configuração. Caso seja preenchido com o endereço do servidor Lincros, o sistema não permite salvar;
- Não envie usuário e senha de acesso em texto aberto por e-mail ou chamado. Combine o repasse das credenciais por um canal seguro.

"Em atenção ao cumprimento de nossas políticas de segurança da informação e privacidade, alguns dados serão ocultados e protegidos".
