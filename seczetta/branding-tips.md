# Branding Tips

## Introduction

SecZetta allows you to upload a custom.css file that gets added to every page that will load within the tool. This document talks about some useful tips and tricks to utilize this custom css to its fullest

## Change a workflow button color

The buttons that execute a workflow look like this in HTML form

```html
<a data-id="d2ef758b-026e-446c-9790-f326919f2eaa" href="/neprofile_dashboard/workflows/d2ef758b-026e-446c-9790-f326919f2eaa/workflow_sessions/new?pid=d195b829-f327-4fa4-aca6-6e4af33b5b42">
    <li class="btn-request">
        <div class="icon-requests"></div>
        Terminate
    </li>
</a>
```

If you want to change the color of that button. You actually have to do it on the child `li` element with the class `btn-request`. Each workflow itself will have an `id`. That id is what is show under the `data-id` attribute on the `a` element. You can see above that the workflow in question has an id of `d2ef758b-026e-446c-9790-f326919f2eaa`. So we can use a css selector with a child element selector as shown below to change the background color of that workflow button:

```css
a[data-id="d2ef758b-026e-446c-9790-f326919f2eaa"] > li{
    background: red !important;
}
```

### Result
![Colored Workflow Button](img/change-workflow-button-color.png)



## Form Header in HTML Text Element

```html
<p class="margin-bottom-small pb_form_heading">Form Title</p>
<hr>
```