@extends('layout')

@section('content')
    <link rel="stylesheet" href="{{asset('/css/home.css')}}">

    <div class="col-md-12 container-fluid">
        @if($items)
            <div class="row">
                @foreach ($items as $item)
                    <div class="col-xs-12 col-sm-4 col-md-3">
                        <div class="thumbnail" style="height: 320px">
                            <div class="pic">
                                <a href="{{ $item->url }}" target="_blank">
                                    <img src="http://106.185.25.253:8000/pics/{{ $item->picfile }}">
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
                        <li class="previous"><a
                                    href="{{ route('search', ['page' => $page - 1, 'query' => $query]) }}"><span
                                        aria-hidden="true">&larr;</span> Newer</a></li>
                    @endif
                    <li class="next"><a href="{{ route('search', ['page' => $page + 1, 'query' => $query]) }}">Older
                            <span aria-hidden="true">&rarr;</span></a></li>
                </ul>
            </nav>
        @else
            <div class="jumbotron">
                <div class="container">
                    <h1>没有找到<em style="color: red">{{ $query }}</em>相关的商品</h1>
                </div>
            </div>
        @endif
    </div>
@endsection
