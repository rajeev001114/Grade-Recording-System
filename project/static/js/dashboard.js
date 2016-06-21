var edx=edx||{};!function($){"use strict";edx.dashboard=edx.dashboard||{},edx.dashboard.donation={},edx.dashboard.donation.DonationView=function(params){var configureForm=function(form,method,url,params){$("input",form).remove(),form.attr("action",url),form.attr("method",method),_.each(params,function(value,key){$("<input>").attr({type:"hidden",name:key,value:value}).appendTo(form)})},firePaymentAnalyticsEvent=function(course){analytics.track("edx.bi.user.payment_processor.visited",{category:"donations",label:course})},addDonationToCart=function(amount,course){return $.ajax({url:"/shoppingcart/donation/",type:"POST",data:{amount:amount,course_id:course}})},view={initialize:function(params){return this.$el=params.el,this.course=params.course,_.bindAll(view,"render","donate","startPayment","validate","startPayment","displayServerError","submitPaymentForm"),this},render:function(){var html=_.template($("#donation-tpl").html(),{});return this.$el.html(html),this.$amount=$('input[name="amount"]',this.$el),this.$submit=$(".action-donate",this.$el),this.$errorMsg=$(".donation-error-msg",this.$el),this.$paymentForm=$(".payment-form",this.$el),this.$submit.click(this.donate),this},donate:function(event){if(event&&event.preventDefault(),this.$submit.addClass("disabled"),this.validate()){var amount=this.$amount.val();addDonationToCart(amount,this.course).done(this.startPayment).fail(this.displayServerError)}else this.$submit.removeClass("disabled")},startPayment:function(data){configureForm(this.$paymentForm,"post",data.payment_url,data.payment_params),firePaymentAnalyticsEvent(this.course),this.submitPaymentForm(this.$paymentForm)},validate:function(){var amount=this.$amount.val(),isValid=this.validateAmount(amount);return isValid?(this.$amount.removeClass("validation-error"),this.$errorMsg.text("")):(this.$amount.addClass("validation-error"),this.$errorMsg.text(gettext("Please enter a valid donation amount."))),isValid},validateAmount:function(amount){var amountRegex=/^\d+.\d{2}$|^\d+$/i;return amountRegex.test(amount)?parseFloat(amount)<.01?!1:!0:!1},displayServerError:function(){this.$errorMsg.text(gettext("Your donation could not be submitted.")),this.$submit.removeClass("disabled")},submitPaymentForm:function(form){form.submit()}};return view.initialize(params),view},$(document).ready(function(){$(".donate-container").each(function(){{var container=$(this),course=container.data("course");new edx.dashboard.donation.DonationView({el:container,course:course}).render()}})})}(jQuery);var edx=edx||{};!function($,gettext,Logger,accessibleModal){"use strict";edx.dashboard=edx.dashboard||{},edx.dashboard.legacy={},edx.dashboard.legacy.init=function(urls){function toggleExpandMessage(e){e.preventDefault(),$(this).closest(".message.is-expandable").toggleClass("is-expanded");var course=$("#upgrade-to-verified").data("course-id");analytics.track("edx.bi.dashboard.upsell_copy.clicked",{category:"user-engagement",label:course})}var notifications=$(".dashboard-notifications");notifications.children().length>0&&notifications.focus(),$(".message.is-expandable .wrapper-tip").bind("click",toggleExpandMessage),$("#failed-verification-button-dismiss").click(function(){$.ajax({url:urls.verifyToggleBannerFailedOff,type:"post"}),$("#failed-verification-banner").addClass("is-hidden")}),$("#upgrade-to-verified").click(function(event){var user=$(event.target).data("user"),course=$(event.target).data("course-id");Logger.log("edx.course.enrollment.upgrade.clicked",[user,course],null)}),$(".email-settings").click(function(event){$("#email_settings_course_id").val($(event.target).data("course-id")),$("#email_settings_course_number").text($(event.target).data("course-number")),"False"===$(event.target).data("optout")&&$("#receive_emails").prop("checked",!0)}),$(".unenroll").click(function(event){$("#unenroll_course_id").val($(event.target).data("course-id")),$("#unenroll_course_number").text($(event.target).data("course-number"))}),$("#unenroll_form").on("ajax:complete",function(event,xhr){200===xhr.status?location.href=urls.dashboard:403===xhr.status?location.href=urls.signInUser+"?course_id="+encodeURIComponent($("#unenroll_course_id").val())+"&enrollment_action=unenroll":$("#unenroll_error").html(xhr.responseText?xhr.responseText:gettext("An error occurred. Please try again later.")).stop().css("display","block")}),$("#pwd_reset_button").click(function(){$.post(urls.passwordReset,{email:$("#id_email").val()},function(){$("#password_reset_complete_link").click()})}),$("#submit-lang").click(function(event){event.preventDefault(),$.post("/lang_pref/setlang/",{language:$("#settings-language-value").val()}).done(function(){$(".settings-language-form").submit()})}),$("#change_email_form").submit(function(){var new_email=$("#new_email_field").val(),new_password=$("#new_email_password").val();return $.post(urls.changeEmail,{new_email:new_email,password:new_password},function(data){data.success?($("#change_email_title").html(gettext("Please verify your new email address")),$("#change_email_form").html("<p>"+gettext("You'll receive a confirmation in your inbox. Please follow the link in the email to confirm your email address change.")+"</p>")):$("#change_email_error").html(data.error).stop().css("display","block")}),!1}),$("#change_name_form").submit(function(){var new_name=$("#new_name_field").val(),rationale=$("#name_rationale_field").val();return $.post(urls.changeName,{new_name:new_name,rationale:rationale},function(data){data.success?location.reload():$("#change_name_error").html(data.error).stop().css("display","block")}),!1}),$("#email_settings_form").submit(function(){return $.ajax({type:"POST",url:urls.changeEmailSettings,data:$(this).serializeArray(),success:function(data){data.success&&(location.href=urls.dashboard)},error:function(xhr){403===xhr.status&&(location.href=urls.signInUser)}}),!1}),accessibleModal(".edit-name","#apply_name_change .close-modal","#apply_name_change","#dashboard-main"),accessibleModal(".edit-email","#change_email .close-modal","#change_email","#dashboard-main"),accessibleModal("#pwd_reset_button","#password_reset_complete .close-modal","#password_reset_complete","#dashboard-main"),$(".email-settings").each(function(index){$(this).attr("id","unenroll-"+index);var trigger="#"+$(this).attr("id");accessibleModal(trigger,"#email-settings-modal .close-modal","#email-settings-modal","#dashboard-main")}),$(".unenroll").each(function(index){$(this).attr("id","email-settings-"+index);var trigger="#"+$(this).attr("id");accessibleModal(trigger,"#unenroll-modal .close-modal","#unenroll-modal","#dashboard-main")}),$("#unregister_block_course").click(function(event){$("#unenroll_course_id").val($(event.target).data("course-id")),$("#unenroll_course_number").text($(event.target).data("course-number"))})}}(jQuery,gettext,Logger,accessible_modal);