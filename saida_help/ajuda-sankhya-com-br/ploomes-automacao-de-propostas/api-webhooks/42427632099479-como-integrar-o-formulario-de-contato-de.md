---
id: "42427632099479"
titulo: "Como integrar o formulário de contato de seu site com o Ploomes"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427632099479-Como-integrar-o-formul%C3%A1rio-de-contato-de-seu-site-com-o-Ploomes"
trilha: "PLOOMES: Automação de propostas  > API & Webhooks"
atualizado_em: "2026-08-03T13:28:33Z"
rotulos: ["sync_hc", "ploomes", "ploomes_5452442", "sync_hash_cdc638533e57"]
---

# Como integrar o formulário de contato de seu site com o Ploomes

**Atenção!** Este artigo é destinado a programadores. Não assumimos qualquer responsabilidade caso seu site fique momentaneamente indisponível durante o desenvolvimento da integração ou durante os testes e assumimos que a pessoa responsável pela integração tenha conhecimento de programação. É altamente recomendável o backup do arquivo de original de sua página e a criação de um ambiente de testes para o período de desenvolvimento.
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

O site da sua empresa é, geralmente, o primeiro canal de contato entre sua organização e o potencial cliente, que muitas vezes utiliza o formulário de contato para enviar mensagens a fim de saber mais sobre seu produto ou serviço. Manter o controle e gerenciar cada um desses Leads é essencial para um processo de vendas assertivo. Tendo isso em mente, uma boa estratégia é integrar o formulário do seu site com o Ploomes para que as informações fornecidas pelos visitantes sejam capturadas e enviadas para seu CRM automaticamente. Este artigo visa explicar, com exemplos práticos, como isto pode ser feito.

Existem muitas linguagens de programação e Frameworks, mas para fins práticos utilizaremos puramente HTML com Javascript. O exemplo pode ser adaptado para qualquer cenário.

Abaixo está um formulário simples em HTML (sem formatação) apenas como exemplo. Não pretendemos e nem esperamos que você o utilize já que ele é extremamente básico e você provavelmente já tem o seu, então ele serve apenas para contextualizar:

```
<table id="contact_table">
  <tbody>
    <tr>
      <td>
        <div >
          <input id="TB_Nome" class="input" name="name" type="text" value="" placeholder="Nome" />
          <br />
        </div>
      </td>
      <td>
        <div >
          <input id="TB_Empresa" class="input" name="empresa" type="text" value="" placeholder="Empresa" />
          <br />
        </div>
      </td>
    </tr>
    <tr>
      <td>
        <div >
          <input id="TB_Telefone" class="input" name="name" type="text" value="" placeholder="Telefone" />
          <br />
        </div>
      </td>
      <td>
        <div >
          <input id="TB_Email" class="input" name="empresa" type="text" value="" placeholder="E-mail" />
          <br />
        </div>
      </td>
    </tr>
  </tbody>
</table>

<input id="submit_button"  onClick="enviarDados()" type="button" value="Enviar" />
```

Deve-se então criar a função **enviarDados** em sua página HTML, na seção reservada para os scripts. O exemplo abaixo mostra um trecho de como seria este script:

```
<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>

<script type="text/javascript">

function enviarDados() {

  document.getElementById("submit_button").disabled = true;

  var empresa = new Object();
  empresa.Name = TB_Empresa.value;
  empresa.TypeId = 1;

  var contato = new Object();

  //Cria a empresa
  $.ajax({type: 'post',url: 'https://public-api2.ploomes.com/Contacts',data: JSON.stringify(empresa),contentType: "application/json; charset=utf-8",headers: {'User-Key' : '1D4CD83C8743D33389C5EFA7AB6B6594BC4B25484CBE5803A99DAE6423AA91A47D51C6501AA2F9746AAB63C434DA4DE7A1475BBF400C2B3A1B61FBFCD97DD50E' },traditional: true,success: function (data) {

    //Empresa criada com sucesso

    var contato = new Object();
    contato.CompanyId = data.value[0].Id; //Atribui o Id da Empresa para o contato, para que fiquem vinculados
    contato.Name = TB_Nome.value;
    contato.Email = TB_Email.value;
    contato.TypeId = 2;

    if(TB_Telefone.value != "")
    {
      var phone = new Object();
      phone.PhoneNumber = TB_Telefone.value;
      phone.TypeId = 1;
      //Cria um Array de telefones e adiciona o telefone recém-criado.
      var phones = new Array(phone);//Adiciona a lista de telefones ao lead
      contato.Phones = phones;
    }

    $.ajax({type: 'post',url: 'https://public-api2.ploomes.com/Contacts',data: JSON.stringify(contato),contentType: "application/json; charset=utf-8",headers: {'User-Key' : '1D4CD83C8743D33389C5EFA7AB6B6594BC4B25484CBE5803A99DAE6423AA91A47D51C6501AA2F9746AAB63C434DA4DE7A1475BBF400C2B3A1B61FBFCD97DD50E' },traditional: true,success: function (data) {
      //contato criado com sucesso
    }});

  }});

}
</script>
```

No trecho de código acima é mostrado como criar um objeto **empresa** e popular com o Nome fornecido no formulário. Em seguida é criado um objeto **pessoa** e preenchido com os demais campos.

Para não ficar muito extenso usamos apenas informações básicas, mas muitas outras podem ser enviadas, como mostrado a seguir. Basta preencher as informações de acordo com sua necessidade e com os campos disponíveis no seu formulário.

Abaixo um exemplo de campos que podem ser manipulados.
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

```
{
  "Id": 693237,
  "TypeId": 1,
  "Name": "Ploomes",
  "LegalName": "Ploomes Sistemas Empresariais S.A.",
  "Register": "17682570000101",
  "CNPJ": "17682570000101",
  "CPF": null,
  "StatusId": 82156,
  "CompanyId": null,
  "RelationshipId": null,
  "LineOfBusinessId": null,
  "OriginId": 141017,
  "NumberOfEmployeesId": null,
  "ClassId": 0,
  "OwnerId": 65005,
  "Birthday": null,
  "Note": null,
  "Email": "berauto.veiculos@globo.com",
  "Website": null,
  "RoleId": null,
  "DepartmentId": null,
  "Skype": null,
  "Facebook": null,
  "StreetAddress": "Av. Francisco Matarazzo, 420",
  "StreetAddressNumber": null,
  "StreetAddressLine2": null,
  "Neighborhood": "Vila Olímpia",
  "ZipCode": 04515030,
  "ForeignZipCode": null,
  "CityId": 2373,
  "StateId": 25,
  "CountryId": 76,
  "CurrencyId": null
}
```

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Além dos campos que são padrões de cada conta, é possível enviar uma lista com campos customizados (**OtherProperties**), que podem ser criados conforme as necessidades do seu negócio.

O link a seguir contém informações adicionais sobre a API do Ploomes:

[Documentação da API do Ploomes](https://sankhya.zendesk.com/hc/pt-br/articles/42427485260695)

Reforçamos que a intenção deste artigo é fornecer um guia prático com exemplos, mas para cada situação ou necessidade será necessário fazer alguns ajustes específicos. Assumimos que a pessoa encarregada de realizar o procedimento tenha conhecimentos em programação.
