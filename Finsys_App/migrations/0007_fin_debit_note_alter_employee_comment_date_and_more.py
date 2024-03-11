# Generated by Django 4.2.6 on 2024-03-11 07:31

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Finsys_App', '0006_fin_delivery_challan_items_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fin_Debit_Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vendor_email', models.EmailField(blank=True, max_length=100, null=True)),
                ('billing_address', models.TextField(blank=True, null=True)),
                ('gst_type', models.CharField(blank=True, max_length=100, null=True)),
                ('gstin', models.CharField(blank=True, max_length=100, null=True)),
                ('place_of_supply', models.CharField(blank=True, max_length=100, null=True)),
                ('debit_note_number', models.CharField(blank=True, max_length=100)),
                ('debit_note_date', models.DateField(blank=True, null=True)),
                ('reference_number', models.IntegerField(blank=True, null=True)),
                ('bill_number', models.CharField(blank=True, max_length=100)),
                ('bill_type', models.CharField(blank=True, max_length=100)),
                ('payment_type', models.CharField(blank=True, max_length=100)),
                ('cheque_number', models.CharField(blank=True, max_length=100)),
                ('upi_id', models.CharField(blank=True, max_length=100)),
                ('bank_account', models.CharField(blank=True, max_length=100)),
                ('description', models.CharField(blank=True, max_length=100)),
                ('document', models.FileField(blank=True, upload_to='file/')),
                ('subtotal', models.IntegerField(default=0, null=True)),
                ('igst', models.FloatField(blank=True, default=0.0, null=True)),
                ('cgst', models.FloatField(blank=True, default=0.0, null=True)),
                ('sgst', models.FloatField(blank=True, default=0.0, null=True)),
                ('price', models.FloatField(blank=True, default=0.0, null=True)),
                ('tax_amount', models.FloatField(blank=True, default=0.0, null=True)),
                ('adjustment', models.FloatField(blank=True, default=0.0, null=True)),
                ('shipping_charge', models.FloatField(blank=True, default=0.0, null=True)),
                ('grandtotal', models.FloatField(blank=True, default=0.0, null=True)),
                ('paid', models.IntegerField(default=0, null=True)),
                ('balance', models.FloatField(blank=True, default=0.0, null=True)),
                ('note', models.TextField(blank=True, null=True)),
                ('status', models.CharField(default='Draft', max_length=150)),
                ('Company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_company_details')),
                ('LoginDetails', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_login_details')),
                ('Vendor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_vendors')),
            ],
        ),
        migrations.AlterField(
            model_name='employee_comment',
            name='date',
            field=models.DateField(default=datetime.date(2024, 3, 11)),
        ),
        migrations.AlterField(
            model_name='fin_attendance_comment',
            name='date',
            field=models.DateField(default=datetime.date(2024, 3, 11)),
        ),
        migrations.AlterField(
            model_name='fin_attendance_history',
            name='date',
            field=models.DateField(default=datetime.date(2024, 3, 11)),
        ),
        migrations.AlterField(
            model_name='holiday_comment',
            name='date',
            field=models.DateField(default=datetime.date(2024, 3, 11)),
        ),
        migrations.CreateModel(
            name='Fin_Recurring_Bills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recurring_bill_number', models.CharField(blank=True, max_length=255, null=True)),
                ('profile_name', models.CharField(blank=True, max_length=255, null=True)),
                ('reference_number', models.IntegerField(blank=True, null=True)),
                ('bill_number', models.CharField(blank=True, max_length=255, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('expected_shipment_date', models.DateField(blank=True, null=True)),
                ('purchase_order_number', models.CharField(blank=True, max_length=255, null=True)),
                ('payment_method', models.CharField(blank=True, max_length=255, null=True)),
                ('cheque_number', models.CharField(blank=True, max_length=255, null=True)),
                ('upi_id', models.CharField(blank=True, max_length=255, null=True)),
                ('bank_account', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('document', models.FileField(blank=True, null=True, upload_to='document')),
                ('sub_total', models.IntegerField(blank=True, null=True)),
                ('cgst', models.IntegerField(blank=True, null=True)),
                ('sgst', models.IntegerField(blank=True, null=True)),
                ('taxAmount_igst', models.IntegerField(blank=True, null=True)),
                ('shipping_charge', models.IntegerField(blank=True, null=True)),
                ('adjustment', models.IntegerField(blank=True, null=True)),
                ('grand_total', models.IntegerField(blank=True, null=True)),
                ('advanceAmount_paid', models.IntegerField(blank=True, null=True)),
                ('balance', models.IntegerField(blank=True, null=True)),
                ('status', models.CharField(blank=True, max_length=255, null=True)),
                ('attachment', models.FileField(blank=True, null=True, upload_to='recurring_bill_attachments')),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_company_details')),
                ('company_payment_terms', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_company_payment_terms')),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_customers')),
                ('repeat_every', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_companyrepeatevery')),
                ('vendor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_vendors')),
            ],
        ),
        migrations.CreateModel(
            name='Fin_Debite_Note_Reference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference_number', models.CharField(blank=True, max_length=150, null=True)),
                ('Company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_company_details')),
                ('LoginDetails', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_login_details')),
                ('debit_note', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_debit_note')),
            ],
        ),
        migrations.CreateModel(
            name='Fin_Debite_Note_History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('action', models.CharField(default='Created', max_length=150)),
                ('Company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_company_details')),
                ('LoginDetails', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_login_details')),
                ('debit_note', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_debit_note')),
            ],
        ),
        migrations.CreateModel(
            name='Fin_Debite_Note_Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.CharField(blank=True, max_length=500, null=True)),
                ('Company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_company_details')),
                ('debit_note', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_debit_note')),
            ],
        ),
        migrations.CreateModel(
            name='Fin_Debit_Note_Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hsn', models.CharField(blank=True, max_length=150, null=True)),
                ('quantity', models.IntegerField(blank=True, default=0, null=True)),
                ('tax_rate', models.FloatField(blank=True, default=0, null=True)),
                ('price', models.FloatField(blank=True, default=0.0, null=True)),
                ('discount', models.FloatField(default=0, null=True)),
                ('total', models.FloatField(blank=True, default=0, null=True)),
                ('debit_note', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_debit_note')),
                ('items', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_items')),
            ],
        ),
    ]
