---
id: "39257386672791"
titulo: "Como importar o XML do S-5002"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39257386672791-Como-importar-o-XML-do-S-5002"
trilha: "Manual do Produto > Pessoas+ > Encargos e Obrigações Legais > Nova DIRF e Informe de Rendimentos > Conferência do IRRF no eSocial"
atualizado_em: "2026-10-02T15:55:56Z"
rotulos: ["XML", "Importação", "eSocial", "Central do eSocial", "Pessoal+", "Informe de Rendimentos", "br.com.sankhya.mgepes.ImportadorEsocial", "Importador XML 5002"]
---

# Como importar o XML do S-5002

**Módulo:**Pessoal+
**Versão Mínima:**5.87
**Caminho de Acesso:** Pessoal+ > Rotinas Folha
**ID da Tela:**br.com.sankhya.mgepes.ImportadorEsocial

---

# Descrição e Usabilidade

A tela **Importador XML 5002** permite importar os arquivos de retorno do eSocial (evento S-5002), para que essas informações sejam utilizadas na geração do **Informe de Rendimentos**.

Essa funcionalidade é especialmente importante para empresas que:

- migraram para o sistema ao longo do ano-calendário;
- realizaram lançamentos de pagamento diretamente no **Portal do eSocial** por meio do **evento S-1210**.

Desde que as informações enviadas ao eSocial estejam corretas, o sistema poderá reaproveitá-las para compor corretamente o Informe de Rendimentos.

⚠️ Utilize **somente XMLs oficiais baixados do Portal do eSocial**, referentes ao retorno do evento **S-5002**.
XMLs gerados por terceiros, exportados de outros sistemas ou manipulados manualmente podem gerar falhas no processamento ou inconsistências no Informe de Rendimentos.

### 1. Descrição da Funcionalidade

O **Importador XML 5002** permite:

- importar arquivos de retorno do evento S-5002;
- disponibilizar esses dados para o Informe de Rendimentos;
- visualizar o status de processamento dos arquivos.

### 2. Pré-requisitos

Antes de utilizar a funcionalidade, verifique:

- Acesso liberado à tela **Importador XML 5002**, concedido pelo usuário administrador do sistema por meio da rotina **Acessos** (Configurações > Controle de Acessos).
- **Versão** do **Sankhya Om** atualizado, módulo **Pessoal+** e **San eSocial** para últimas versões disponíveis.
- Arquivo de retorno do eSocial disponível:
  - evento S-5002;
  - formato XML;
  - compactado em arquivo .zip;
  - o XML foi **baixado diretamente do Portal do eSocial**.

### 3. Jornada de Uso

[GIF animado: Imagem 1: 3. Jornada de Uso](https://ajuda.sankhya.com.br/hc/article_attachments/39258381420183)

1. Acesse a tela **Importador XML 5002** (Pessoal+ > Rotinas Folha).
2. Clique no botão **Upload**.
3. Selecione o arquivo compactado (.zip) contendo os XMLs do S-5002.

   Para importar arquivos da **Central do eSocial** (Pessoal+ > Rotinas Folha):

   - **1 arquivo XML**
     → Compacte o arquivo em formato .zip.
   - **Mais de um arquivo XML**
     → Crie uma pasta;
     → Adicione os arquivos XML;
     → Compacte a pasta em formato .zip.

   O sistema iniciará automaticamente o processamento.
4. Após o envio do arquivo:

   - Um **pop-up** será exibido com o andamento do processo.
   - A tela apresentará duas grades:

     - Grade superior - **Importações eSocial**

       **→** Exibe o **arquivo pai** (arquivo principal importado).
     - Grade inferior - **Importações eSocial Detalhes**

       → Exibe os **arquivos filhos** (XMLs individuais do S-5002).

### 4. Pontos de Atenção

- Os **filtros da tela** são utilizados para localizar os arquivos pai exibidos na grade **Importações eSocial**.
- O sistema **ignora automaticamente** arquivos que **não estejam no formato XML**.
- Caso sejam importados arquivos XML que **não correspondam ao retorno do evento S-5002**, o sistema tentará processá-los, porém o processamento será finalizado **com erro no status**.
- O status do arquivo pai será atualizado **somente após o processamento de todos os arquivos filhos**.

⚠️ Enquanto o processamento não for concluído, o status permanecerá como **Pendente**.

### 5. Dicas de Usabilidade

- Sempre valide se os XMLs são do evento S-5002 antes da importação.
- Confirme se os arquivos foram **baixados diretamente do Portal do eSocial**.
- Utilize nomes de arquivos organizados para facilitar a identificação.
- Aguarde a finalização completa antes de validar os dados.
- Utilize os filtros para localizar rapidamente importações anteriores.

💡Mantenha uma pasta separada com os XMLs oficiais do Portal por ano-calendário para facilitar reprocessamentos futuros.

## Perguntas Frequentes (FAQ)

**1. Posso importar arquivos que não sejam do evento S-5002?**

Caso sejam importados arquivos XML que não correspondam ao evento **S-5002**, o sistema até tenta processá-los, porém o processamento será finalizado com erro no status.

Além disso, recomenda-se utilizar **apenas XMLs oficiais do Portal do eSocial**.

**2. O sistema aceita arquivos XML sem compactação?**

Não. Os arquivos devem estar no formato .zip para serem importados.

**3. Importei o arquivo, mas ele continua com status Pendente. Por quê?**

O status permanece como **Pendente** enquanto o sistema ainda está processando os arquivos filhos.
Ele só será atualizado após a finalização completa do processamento.

**4. Posso importar mais de um XML ao mesmo tempo?**

Sim. Basta compactar todos os arquivos em uma única pasta .zip.

**5. O que acontece se houver arquivos inválidos dentro do .zip?**

- Arquivos que não estejam no formato XML são ignorados;
- XMLs que não sejam do evento **S-5002** serão processados, porém retornarão erro no status;
- XMLs de outras origens que não sejam o **Portal do eSocial** também podem apresentar erro estrutural.

**6. Essa importação substitui informações da folha?**

Não diretamente.

Os dados importados são utilizados principalmente para compor o Informe de Rendimentos.

**7. Em quais situações devo usar essa tela?**

- quando houve migração de sistema durante o ano-calendário;
- quando os dados foram enviados diretamente pelo **Portal do eSocial** (S-1210);
- quando é necessário complementar informações para o **Informe de Rendimentos**;
- quando você possui os **XMLs oficiais de retorno S-5002 baixados do Portal do eSocial**.

## Artigos Relacionados

- [Nova DIRF/eSocial 2025](https://ajuda.sankhya.com.br/hc/pt-br/articles/37361211258647)
- [Central do eSocial](https://ajuda.sankhya.com.br/hc/pt-br/articles/7064222145175)
- [Relatório S-5002 – Conferência de Imposto de Renda Retido na Fonte por Trabalhador](https://ajuda.sankhya.com.br/hc/pt-br/articles/37202771074071)
- [Informe de Rendimentos (DIRF): nova geração via Folha de Pagamento ou eSocial](https://ajuda.sankhya.com.br/hc/pt-br/articles/20941208310167)
