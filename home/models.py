from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.core.models import Page, Orderable
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.fields import RichTextField, BlockField

from wagtail.snippets.models import register_snippet
from wagtail.models import BootstrapTranslatableMixin
from django.db import migrations
from wagtail.models import BootstrapTranslatableModel
from wagtail.search import index

class HomePage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]
    
class ResearchPage(Page):
    name = models.CharField(max_length=200)
    description = RichTextField(blank=False)
    feed_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    search_fields = Page.search_fields + [
        index.SearchField('name'),
    ]
    
    content_panels = Page.content_panels + [
        FieldPanel('name'),
        FieldPanel('description', classname="full"),
    ]
    
    promote_panels = [
        MultiFieldPanel(Page.promote_panels, "Common page configuration"),
        FieldPanel('feed_image'),
    ]


@register_snippet
class Advert(BootstrapTranslatableMixin, models.Model):
    name = models.CharField(max_length=255)
    class Meta(BootstrapTranslatableMixin.Meta):
        verbose_name = 'adverts'
        
class Migration(migrations.Migration):
    dependencies = [
        ('keisuu', '0002_bootstraptranslations'),
    ]
    operations = [
        BootstrapTranslatableModel('keisuu.Advert'),
    ]
