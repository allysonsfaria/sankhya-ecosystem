---
id: "39383900094615"
titulo: "257 : Rejeicao: Solicitante nao habilitado para emissao da NF-e"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/39383900094615-257-Rejeicao-Solicitante-nao-habilitado-para-emissao-da-NF-e"
trilha: "Solução de Problemas > Rejeições: NF-e / NFS-e / NFC-e - Reforma tributária "
atualizado_em: "2026-10-09T02:54:34Z"
rotulos: ["Configuração", "Parceiro", "NF-e", "SEFAZ", "Rejeição", "Erro", "Artigo criado KCS", "CVE - KCS"]
---

# 257 : Rejeicao: Solicitante nao habilitado para emissao da NF-e

**"257 Rejeição: Solicitante não habilitado para emissão da NF-e"**

### SITUAÇÃO

Ao tentar importar dados cadastrais de parceiros pela opção **"Importar dados cadastrais da SEFAZ"**, disponível em **"Outras Opções"** da tela **"Parceiros"** (Configurações » Cadastros » Parceiros), o sistema apresenta a rejeição 257, informando que o solicitante não está habilitado para emissão da NF-e. A mesma rejeição pode aparecer na opção **"Atualizar situação cadastral SEFAZ/SUFRAMA"**. Nesse caso, o sistema acrescenta a orientação "Verificar a empresa do certificado informada no parâmetro EMPPADCERTDIG". Esta situação impede a obtenção automática dos dados cadastrais do parceiro, mesmo quando o CNPJ e a Inscrição Estadual estão corretos.

### SOLUÇÃO

Esta rejeição é devolvida pela SEFAZ e se refere à **empresa que faz a consulta**, e não ao parceiro. Siga as orientações abaixo:

**(1)** Na tela **"Preferências"**, confira o parâmetro **"EMPPADCERTDIG"** (Empresa padrão para utilização do certificado digital). O certificado digital e o CNPJ dessa empresa são os enviados à SEFAZ na consulta. Ela deve ser uma empresa emissora de NF-e, com certificado digital válido. Se houver outra empresa informada, ajuste o parâmetro e refaça a importação.

**(2)** Se a empresa estiver correta e a rejeição continuar, a restrição é da SEFAZ. Nesse caso, realize o **"Cadastro manual"** do parceiro na tela **"Parceiros"** (Configurações » Cadastros » Parceiros), preenchendo todos os campos obrigatórios, incluindo CNPJ, Razão Social, Inscrição Estadual e endereço completo.

**(3)** Como alternativa, utilize a opção de importação de dados da **"Receita Federal (ReceitaWS)"**, também em **"Outras Opções"** da tela Parceiros, para obter informações básicas do parceiro (somente para CNPJ). Observe que esta opção não retorna a Inscrição Estadual, sendo necessário preenchê-la manualmente após a importação.

**(4)** Caso necessite de esclarecimentos específicos sobre a rejeição ou deseje solicitar a liberação da consulta, entre em contato diretamente com a SEFAZ do estado do parceiro que está sendo consultado.

### CAUSA

A rejeição 257 indica que o solicitante da consulta, ou seja, a empresa cujo certificado digital foi utilizado, não está habilitado para emissão de NF-e. Na importação e na atualização da situação cadastral, o Sankhya utiliza sempre o certificado da empresa informada no parâmetro **EMPPADCERTDIG**.

Além disso, as Secretarias da Fazenda (SEFAZ) de cada Unidade Federativa podem estabelecer restrições na consulta cadastral, permitindo que apenas contribuintes habilitados para emissão de NF-e dentro do próprio estado realizem consultas aos dados de parceiros localizados naquela UF.

Dessa forma, mesmo que o CNPJ da empresa solicitante e do parceiro estejam corretos, a consulta retorna a **"Rejeição 257"** quando a empresa que está realizando a consulta (a do parâmetro EMPPADCERTDIG) não pertence à mesma UF do parceiro consultado ou não está habilitada para emitir NF-e naquele estado.

O sistema ERP Sankhya utiliza o serviço oficial disponibilizado pela SEFAZ por meio de WSDL via protocolo SOAP. Portanto, o retorno da rejeição é originado diretamente do serviço da própria SEFAZ, não sendo uma limitação do sistema.

O campo **"Situação Cadastral SEFAZ"** (aba Fiscal do cadastro de parceiros) mostra a situação do **parceiro** consultado, Habilitado ou Não Habilitado, conforme o retorno da SEFAZ. Ele só é atualizado quando a consulta é concluída. Quando ocorre a rejeição 257, ele não é alterado e, por isso, não tem relação com a causa desta rejeição.
