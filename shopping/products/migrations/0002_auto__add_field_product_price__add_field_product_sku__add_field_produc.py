# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Product.price'
        db.add_column(u'products_product', 'price',
                      self.gf('django.db.models.fields.IntegerField')(default=0.0),
                      keep_default=False)

        # Adding field 'Product.sku'
        db.add_column(u'products_product', 'sku',
                      self.gf('django.db.models.fields.CharField')(default='abc', max_length=160),
                      keep_default=False)

        # Adding field 'Product.inventory'
        db.add_column(u'products_product', 'inventory',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Product.price'
        db.delete_column(u'products_product', 'price')

        # Deleting field 'Product.sku'
        db.delete_column(u'products_product', 'sku')

        # Deleting field 'Product.inventory'
        db.delete_column(u'products_product', 'inventory')


    models = {
        u'products.product': {
            'Meta': {'ordering': "['-id']", 'object_name': 'Product'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image1': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'inventory': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'price': ('django.db.models.fields.IntegerField', [], {'default': '0.0'}),
            'sku': ('django.db.models.fields.CharField', [], {'default': "'abc'", 'max_length': '160'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'})
        }
    }

    complete_apps = ['products']