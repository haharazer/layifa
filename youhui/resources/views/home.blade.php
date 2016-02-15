@extends('layout')

@section('content')
    <link rel="stylesheet" href="{{asset('/css/home.css')}}">

    <div class="jumbotron">
        <div class="container">
            <h1>标题</h1>
        </div>
    </div>

    <div class="col-md-12 container-fluid">
        <div class="row">
            @foreach ($items as $item)
                <div class="col-xs-12 col-sm-4 col-md-3">
                    <div class="thumbnail" style="height: 320px">
                        <div  class="pic">
                            <a href="{{ $item->url }}" target="_blank">
                                <img src="/pics/{{ $item->picfile }}">
                            </a>
                        </div>
                        <div class="caption">
                            <h2 class="itemName">
                                <a href="{{ $item->url }}" target="_blank">
                                    <span class="black">{{ $item->title }}</span>
                                    <span class="red">{{ $item->price }}</span>
                                </a>
                            </h2>
                            <div class="timeInfo">
                                <span class="time">{{ date('m-d H:i', $item->timestamp) }}</span>
                            </div>
                        </div>
                    </div>
                </div>
            @endforeach
        </div>

        <nav>
            <ul class="pager">
            @if($page == 1)
                <li class="previous disabled"><a href="#"><span aria-hidden="true">&larr;</span> Newer</a></li>
            @else
                <li class="previous"><a href="{{ route('home', ['page' => $page - 1]) }}"><span aria-hidden="true">&larr;</span> Newer</a></li>
            @endif
            <li class="next"><a href="{{ route('home', ['page' => $page + 1]) }}">Older <span aria-hidden="true">&rarr;</span></a></li>
          </ul>
        </nav>
    </div>
@endsection