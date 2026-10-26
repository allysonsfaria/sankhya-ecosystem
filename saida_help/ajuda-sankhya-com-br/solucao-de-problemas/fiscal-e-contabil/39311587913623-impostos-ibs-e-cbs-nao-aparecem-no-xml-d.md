---
id: "39311587913623"
titulo: "Impostos IBS e CBS não aparecem no XML da Nota Fiscal"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39311587913623-Impostos-IBS-e-CBS-n%C3%A3o-aparecem-no-XML-da-Nota-Fiscal"
trilha: "Solução de Problemas > Fiscal e Contábil "
atualizado_em: "2026-10-22T12:42:51Z"
rotulos: ["Configuração", "NF-e", "XML", "Impostos", "Artigo criado KCS", "Alíquotas de CBS", "Alíquotas de IBS", "Fiscal/Contábil - KCS"]
---

# Impostos IBS e CBS não aparecem no XML da Nota Fiscal

**MENSAGEM**

Os impostos IBS e CBS não são exibidos no arquivo XML da Nota Fiscal, mesmo após a configuração das alíquotas e realização do cálculo dos impostos no sistema.

**SITUAÇÃO**

Ao emitir uma nota fiscal de teste após configurar as alíquotas de **"IBS"** e **"CBS"** para a reforma tributária, o sistema calcula corretamente os impostos na tela **"Consultar/Alterar Dados de Impostos"** (Comercial Avançado Consultar/Alterar Dados de Impostos). Porém, ao consultar o arquivo XML gerado, as tags correspondentes aos novos impostos não aparecem no documento.

**SOLUÇÃO**

Para que as tags de IBS e CBS apareçam corretamente no XML, siga os passos abaixo:

**(1)** Acesse a tela **"Empresa"** (Comercial Preferências Empresa).
**(2)** Navegue até a aba **"Documentos Fiscais Eletrônicos"** e selecione **"NFe"** **"Nota Técnica"**.
**(3)** Ative a **"Nota Técnica RTC V1.10"**, que habilita o destaque dos novos impostos no XML.
**(4)** Acesse a tela **"Alíquota IBS"** e **"Alíquota CBS"** (Comercial Arquivo Cadastros Impostos Alíquotas) e verifique se o campo **"Vigência Início"** está configurado corretamente com a data de início da obrigatoriedade.
**(5)** Verifique se as alíquotas estão cadastradas no campo correto dentro da **"Regra de Alíquota"**. Certifique-se de que os percentuais de IBS e CBS estão nos campos específicos para cada imposto.
**(6)** Acesse a tela **"TOP - Tipo de Operação"** (Comercial Arquivo Cadastros Tipos de Operação - TOP) e configure o layout para que os impostos IBS e CBS sejam calculados. Marque todos os campos relacionados aos novos impostos.
**(7)** Emita uma nova nota fiscal de teste e verifique se os impostos foram calculados corretamente na tabela **"TGFDIN"**.
**(8)** Consulte o arquivo XML gerado e verifique se as tags de IBS e CBS estão presentes no documento.

**Observação:** Para que as tags apareçam no XML, é obrigatório que os impostos sejam calculados corretamente. Se os valores não estiverem na tabela **"TGFDIN"**, as tags não serão geradas no arquivo XML.

**CAUSA**

O problema ocorre devido a uma ou mais das seguintes causas:

- A **"Nota Técnica RTC V1.10"** não está ativada na configuração da empresa.
- O campo **"Vigência Início"** nas alíquotas de IBS e CBS está configurado com data incorreta ou futura.
- As alíquotas estão cadastradas no campo errado dentro da regra de alíquota.
- O **"Layout do TOP"** não está configurado para calcular os impostos IBS e CBS.
- Os impostos não foram calculados corretamente e, portanto, não constam na tabela **"TGFDIN"**, impedindo a geração das tags no XML.

  Importante: Deve ser verificado é a consistência entre o CST e o CCLASSTRIB cadastrados para o IBS e para o CBS. Como esses dois impostos compartilham uma única tag no XML da nota (a tag IBSCBS), é obrigatório que ambos possuam exatamente o mesmo código de CST (000, 200 ou 410) e o mesmo código de Classificação Tributária (CCLASSTRIB) cadastrados em suas respectivas regras de alíquota.

  Caso haja divergência entre esses códigos, a tag pode simplesmente não ser gerada no XML, mesmo que as alíquotas estejam corretas, a vigência esteja válida e os valores já constem na tabela TGFDIN.

   Essa verificação deve ser feita na **tela de Alíquota IBS e Alíquota CBS**, ou diretamente na Regra de Alíquota vinculada ao TOP utilizado na nota, e representa uma das causas mais recorrentes desse tipo de problema.
