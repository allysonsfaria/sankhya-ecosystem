---
id: "360043195253"
titulo: "580 Rejeição: Falha no Schema XML específico para o modal"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360043195253-580-Rejei%C3%A7%C3%A3o-Falha-no-Schema-XML-espec%C3%ADfico-para-o-modal"
trilha: "Solução de Problemas > Mensagens de validação da SEFAZ"
atualizado_em: "2026-07-22T16:06:53Z"
rotulos: ["#criadoRoger", "ERROMDFE", "ERROCTE", "#RevisadoBraga", "MDF-e", "Configuração", "Veículos", "Parceiro", "XML", "SEFAZ", "CPF", "580", "Verifique campos obrigatórios e ajuste dados", "Erro na validação do Schema XML pelo SEFAS", "Falha no Schema XML específico para o modal", "namespace", "580 Rejeição:", "Rejeição 580"]
---

# 580 Rejeição: Falha no Schema XML específico para o modal

**![Imagem 1: MENSAGEM:](https://ajuda.sankhya.com.br/hc/article_attachments/16513762159511) MENSAGEM:**

580 Rejeição: Falha no Schema XML específico para o modal.

**![Imagem 2: SOLUÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16513778488983) SOLUÇÃO:**

O Schema XML faz algumas validações em seu comportamento. Assim, para solucionar esse erro, verifique essas validações e faça os ajustes necessários para que estejam adequadas:

![Imagem 3: Campos do cadastro de Veículo- Rotina: Configurações » Cadastros » Veículos](https://ajuda.sankhya.com.br/hc/article_attachments/16513762179223) Campos do cadastro de Veículo- Rotina: Configurações » Cadastros » Veículos

- **Placa**: Obrigatoriamente deve ter 3 letras e 4 números (para veículos emplacados no padrão antigo) e também o novo formato de placas padrão Mercosul (4 letras e 3 números);
- **CapKG**: Deve conter de 1 a 6 dígitos inteiros, não é aceito valor decimal.
- **CapM3**: Deve conter de 1 a 3 dígitos inteiros, não é aceito valor decimal.
- **RNTRC**: Campo só pode receber valor numéricos, não pode ter letra na codificação.

**![Imagem 4: IMPORTANTE: O RNTRC deverá conter obrigatoriamente 8 dígitos , conforme leiaute da MDF-e. Caso o RNTRC tenha apenas 7…](https://ajuda.sankhya.com.br/hc/article_attachments/16513762182295) IMPORTANTE:** O RNTRC deverá conter obrigatoriamente **8 dígitos**, conforme leiaute da MDF-e. Caso o RNTRC tenha apenas 7 dígitos, excluindo-se os zeros, deverão ser preenchidos zeros à esquerda até que se completem 8 dígitos. Caso o veículo seja da empresa, ou seja, o campo '**Veículo da empresa"** está marcado no cadastro do veículo, insira o RNTRC no cadastro da empresa, na tela Configurações » Cadastros » Empresas.

- **RENAVAM:** Código possui de 9 a 11 dígitos
- **Tara**: Deve conter de 1 a 6 dígitos inteiros, não é aceito valor decimal.
- **Tipo de Rodado:**Preenchimento obrigatório são aceitos os valores (01, 02, 03, 04, 05 ou 06).
- **Tipo de Carroceria:** Preenchimento obrigatório são aceitos os valores (01, 02, 03, 04 ou 05).
- **Tipo de Proprietário:** Preenchimento obrigatório são aceitos os valores (00, 01 ou 02).

![Imagem 5: Campos do Cadastro do Parceiro- Rotina: Configurações » Cadastros » Parceiros](https://ajuda.sankhya.com.br/hc/article_attachments/16513762184727) Campos do Cadastro do Parceiro- Rotina: Configurações » Cadastros » Parceiros

- **"Razão ou Nome do Proprietário":** Preenchimento obrigatório (sem espaços em branco no início/fim do nome ou carácter), máximo 60 carácter.

- **CPF do Motorista:** 11 dígitos (sem pontos ou hifens)

**![Imagem 6: OBSERVAÇÃO:](https://ajuda.sankhya.com.br/hc/article_attachments/16513778500759) OBSERVAÇÃO:**

Caso o parâmetro "**RNTRCFROTAPROP"** esteja habilitado, informe 99999999 no campo RNTRC no cadastro do Veículo.

(1)** DICAS:**

**(2)** Utilizamos o validador disponível no site <https://dfe-portal.svrs.rs.gov.br/MDFE/ValidadorXML> para validar o xml de conferência do MDF-e, pois nesta validação é retornada qual informação deve ser ajustada.

**(2)**Caso seja necessário consultar validações de tags, baixe o Manual do MDF disponível em [https://dfe-portal.sefazvirtual.rs.gov.br/Mdfe/Documentos#](https://dfe-portal.sefazvirtual.rs.gov.br/Mdfe/Documentos)

**![Imagem 7: CAUSA:](https://ajuda.sankhya.com.br/hc/article_attachments/16513778513303) CAUSA:**

Ocorre porque a SEFAZ não efetua a validação campo a campo do Grupo de Informações do Modal <**infModal**>. Sendo assim, se algum campo estiver incorreto, ele irá apresentar a referida mensagem. Quando essa rejeição ocorre, é uma rejeição **genérica da SEFAZ**, pois a SEFAZ não indica exatamente o que está de errado no XML.
