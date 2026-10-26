---
id: "https://developer.sankhya.com.br/reference/gerando-tokens-de-integração-no-sankhyaom"
titulo: "Gerando Tokens de Integração no SankhyaOm"
url: "https://developer.sankhya.com.br/reference/gerando-tokens-de-integração-no-sankhyaom"
atualizado_em: "2025-11-10T23:39:09.000Z"
---

# Gerando Tokens de Integração no SankhyaOm

Agora vamos gerar o Token na tela [Configurações Gateway](https://ajuda.sankhya.com.br/hc/pt-br/articles/10007620733463-Configura%C3%A7%C3%B5es-Gateway) disponível no SankhyaOm. Veja no vídeo a seguir como proceder:

<HTMLBlock>{`
<iframe width="100%" height="400px" src="https://www.youtube.com/embed/H36Q1J_cxNI" title="Embed videos and playlists" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
`}</HTMLBlock>

<br />

### Liberando IP´s do Gateway no Firewall

Por padrão, Firewalls bloqueiam conexões de aplicativos com a Internet e o uso de portas específicas, como medida de segurança. No entanto, essa configuração pode interferir no funcionamento das APIs da Sankhya, que necessitam de acesso a portas específicas para se comunicarem com servidores remotos do Gateway. Portanto é necessário adicionar os IPs dos nossos servidores à lista de permissões do firewall, garantindo a liberação do tráfego necessário.

> 🚧 Atenção
>
> Verifique se o firewall do servidor de aplicação do SankhyaOm permite conexões de saída para os IPs dos servidores Sankhya. Caso contrário, inclua-os manualmente nas regras de exceção para evitar falhas de comunicação.
>
> **144.22.228.211** e **144.22.217.141** para o ambiente de Produção e
>
> **150.230.86.234** e **144.22.173.39** para o ambiente de Sandbox (testes).

<HTMLBlock>{`
<div class="center">
 <a class="button_background button_size"
                    href="https://ajuda.sankhya.com.br/hc/pt-br/articles/360044982114-Orienta%C3%A7%C3%B5es-para-configura%C3%A7%C3%A3o-de-acesso-externo-das-solu%C3%A7%C3%B5es-Sankhya-"
                   target= "_blank" rel="noopener noreferrer">Configurações de acesso externo</a>
</div>

<style>
    
   .center {
       display: flex;
       justify-content: center;
       align-items: center;
       height: 100px;
   }
  
   .button_size {
       background-color: #4CAF50;
  		 border: none;
  		 color: white;
 			 padding: 15px 32px;
  		 text-align: center;
       text-decoration: none !important;
       display: inline-block;
       font-size: 16px;
       margin: 4px 2px;
       cursor: pointer;
       box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2), 0 6px 20px 0 rgba(0,0,0,0.19);

    }

    .button_background {
        background-color: #66cc66;
        color: #fff !important;
    }

</style>
`}</HTMLBlock>
