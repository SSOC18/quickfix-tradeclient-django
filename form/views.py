from django.views.generic import TemplateView
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from form import tasks
from form.forms import HomeForm

import io
import os
import pika
import pandas as pd
import plotly.graph_objs as go
import plotly.offline as offline


def plot(request):
    data = [
        go.Scatter(
            x=[1, 2, 3],
            y=[4, 5, 6],
            mode = 'markers',
        )
    ]

    layout = go.Layout(
          title="Scatter Plot",
        )

    figure = go.Figure(data=data, layout=layout)
    
    offline.plot(figure)

    return render_to_response('temp-plot.html')

def success(request):
    return HttpResponse('Order Accepted!')

class HomeView(TemplateView):
    template_name = os.path.join('templates/','form.html')

    def get(request):
        if request.method == 'GET':
            form = HomeForm()

            args = {'form': form}
            return render(request, 'form/form.html', args)

        else:
            form = HomeForm(request.POST)
            form = form.data
            if form != 0: #if form.is_valid() was not working (FALSE so jumped the loop)
                action = form['action']
                version = form['version']
                clordid = form['clordid']
                price = form['price']
                symbol = form['symbol']
                ordqty = form['ordqty']
                side = form['side']
                ordtype = form['ordtype']
                timeinforce = form['timeinforce']
                senderid = form['senderid']
                targetid = form['targetid']
                targetsubid = form['targetsubid']
                body = "{"+f"{action}"+""+f" {version}"+""+f" {clordid}"+""+f" {price}"+""+f" {symbol}"+""+f" {ordqty}"+""+f" {side}"+""+f" {ordtype}"+""+f" {timeinforce}"+""+f" {senderid}"+""+f" {targetid}"+""+f" {targetsubid}"+"}"

                connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
                channel = connection.channel()
                channel.queue_declare(queue='orders')
                channel.basic_publish(exchange='',
                      routing_key='orders',
                      body=body)
                connection.close()
            else:
                raise Http404

            return HttpResponseRedirect('/form/success/')