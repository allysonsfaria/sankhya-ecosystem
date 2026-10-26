---
id: "42427030532119"
titulo: "Manual Recuperador de Tributos"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427030532119-Manual-Recuperador-de-Tributos"
trilha: "ASIS: Auditoria e validação de erros fiscais > Base de conhecimento > Análise e Auditoria"
atualizado_em: "2026-08-03T12:43:08Z"
rotulos: ["asis", "sync_hc", "asis_52907642286099", "sync_hash_a5c9d2c0bd55"]
---

# Manual Recuperador de Tributos

### Exclusão de ICMS da base de cálculo de Pis e Cofins

É obrigatório o cadastro das Empresas para geração do relatório de exclusão quando feito pelos documentos fiscais.

Os documentos fiscais aceitos são (NF-e e, NFC-e e/ou SAT) e o TXT da EFD- contribuições.

A importação da EFD-contribuições na plataforma gera cadastro da empresa titular da obrigação, automaticamente. Registros C100 e C170.

### Exclusão de ISS da base de cálculo de Pis e Cofins

Somente é possível, atualmente na plataforma, realizar a exclusão do ISS pelo arquivo TXT da EFD - Contribuições.

A importação da EFD - Contribuições na plataforma, gera o cadastro automático da empresa titular da obrigação. Para que o relatório retorne com resultado é necessário possuir os registros A100 e A170, contendo o valor do ISS no registro A100, no Bloco A.

1ª ETAPA (Gestão da conta)

Na Homepage da ferramenta deverá acessar o aplicativo Gestão da conta. Posteriormente na área Empresas cadastre na funcionalidade <Novo>.

![Imagem 1: Na Homepage da ferramenta deverá acessar o aplicativo Gestão da conta. Posteriormente na área Empresas cadastre na…](https://ajuda.sankhya.com.br/hc/article_attachments/42427026411543)

Na importação do TXT a plataforma faz o cadastro automático no aplicativo Gestão da conta.

2ª ETAPA (UPLOAD .XML ou TXT)

A importação dos documentos fiscais eletrônicos (NF-e e, NFC-e e/ou SAT) e do TXT da EFD, poderá ser realizada manualmente através do botão UPLOAD ou pelo Robô de Importação Automática, disponível na Central de Downloads.

OBS: para upload de arquivos compactados é obrigatório que estejam na extensão .ZIP, tanto via UPLOAD quanto pelo Robô de importação Automática.

## Novo Processo de Exclusão

Com as etapas de cadastro de empresas e upload das obrigações, basta acessar o aplicativo Recuperador de Tributos e ir até o ícone Exclusão do ICMS da BC do PIS/COFINS, clicar em Novo Processo e preencher as informações necessárias, conforme telas abaixo:

![Imagem 2: Com as etapas de cadastro de empresas e upload das obrigações, basta acessar o aplicativo Recuperador de Tributos e ir…](https://ajuda.sankhya.com.br/hc/article_attachments/42427026516247)

![Imagem 3: Com as etapas de cadastro de empresas e upload das obrigações, basta acessar o aplicativo Recuperador de Tributos e ir…](https://ajuda.sankhya.com.br/hc/article_attachments/42427047682071)

Nome - Nome para o processo (Opcional)

Empresa - Selecionar a Empresa que vai realizar a Apuração (Obrigatório)

Estado - Estado da Empresa (Opcional)

Mês Ref. Início - Período da Exclusão (Obrigatório, e é necessário respeitar a formação solicitada AAAAMM)

Obrigação de origem - Selecionar a fonte da exclusão se é por Notas ou EFD Contribuição (Obrigatório)

Para ter acesso ao relatório, basta acessar Exclusão do ICMS da BC do PIS/COFINS e clicar na
caixa do lado esquerdo e realizar o download em Excel. Pronto!!!

![Imagem 4: Para ter acesso ao relatório, basta acessar Exclusão do ICMS da BC do PIS/COFINS e clicar na caixa do lado esquerdo e…](https://ajuda.sankhya.com.br/hc/article_attachments/42427063603223)

IMPORTANTE

A exclusão do ICMS da Base de Cálculo do ICMS através da EFD Contribuições é realizada
exclusivamente através dos Registros A100/A170 e C100/C170.

Os demais registros do arquivo (Ex: C175, C180, C181, C185, F500, F525, F550 e F560)
não possuem informações do ICMS destacado nos documentos fiscais, portanto,
impossibilitam a realização do cálculo.

Importar os arquivos .xml dos documentos fiscais eletrônicos (NF-e, NFC-e e/ou
SAT) e selecionar a opção “DOCS” no campo Obrigação de Origem.

Nota:  A exclusão é realizada para base de cálculo que ainda não foi ajustada com a dedução de ICMS.

Para que a apuração da exclusão do ICMS/ISS seja realizada de forma correta, é fundamental que os documentos estejam devidamente preenchidos e consistentes. Recomendamos, portanto, que sejam analisadas as auditorias do XML e da EFD Contribuições, a fim de assegurar que os cálculos sejam processados de maneira precisa e em conformidade com a legislação

## Status de Processamento

![Imagem 5: Status de Processamento](https://ajuda.sankhya.com.br/hc/article_attachments/42427063678359)

É possível diagnosticar o erro passando o mouse por cima do X.
